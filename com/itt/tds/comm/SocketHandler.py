try:
    import socket
    from threading import Thread
    import threading
    from com.itt.tds.comm.TDSRequest import TDSRequest
    from com.itt.tds.comm.TDSSerializerFactory import TDSSerializerFactory
    from com.itt.tds.logs.LogManager import LogManager
    from com.itt.tds.comm.RequestDispatcher import RequestDispatcher

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'SocketHandler', 'Import Module', error.__str__(), str(error))


class SocketHandler(Thread):
    s_socket = None

    def __init__(self, socket, h_name, p_number, clientsocket, addr):
        super().__init__(target=None, args=())
        SocketHandler.s_socket = socket
        self.h_name = h_name
        self.p_number = p_number
        self.reqsocket = clientsocket
        self.addr = addr

    def run(self):
        """
            Description : Function which will run for each thread for 
            SocketHandler class. It calls get_request function to 
            accept a client connection request and process the request
            according to the request method.

        """
        request_data, addr = self.get_request()
        tds_serializer = TDSSerializerFactory.get_serializer()
        request = tds_serializer.deserialize(request_data)
        controller = RequestDispatcher.get_controller(request)
        response = controller.process_request(request)
        response.set_source_ip(self.h_name)
        response.set_source_port(self.p_number)
        response.set_destination_ip(self.addr[0])
        response.set_destination_port(self.addr[1])
        response_data = tds_serializer.serialize(response)
        self.write_response(response_data)

    def get_request(self):
        return (self.reqsocket.recv(1024), self.addr)

    def write_response(self, response):
        """
            Description : Function is responsible to write into socket object
            and send response back to client
        """
        self.reqsocket.send(response)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
h_name = socket.gethostname()
p_number = 9994
server.bind((h_name, p_number))
server.listen(5)
server_processes = []

while True:
    clientsocket, addr = server.accept()
    if addr:
        print (threading.active_count())
        server_processes.append(SocketHandler(server, h_name, p_number, clientsocket, addr).start())


# waiting for the threads to get completed
for x in server_processes:
    x.join()
