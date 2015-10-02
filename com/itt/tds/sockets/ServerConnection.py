
try:
    import socket
    from com.itt.tds.sockets.TDSResponse import TDSResponse
    from com.itt.tds.sockets.TDSRequest import TDSRequest
    from com.itt.tds.sockets.TDSSerializerFactory import TDSSerializerFactory
    from com.itt.tds.logs.LogManager import LogManager
except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'ServerConnection', 'Import Module', error.__str__(), str(error))


class ServerConnection:

    def __init__(self):
        """
            Description: Initialization function for ServerConnection Class.
            It creates a socket at server end to handle the client request
            on specific port.

            Argument : None

            Return Type : None
        """
        self.s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.h_name = socket.gethostname()
        self.p_number = 9994
        self.s_socket.bind((self.h_name, self.p_number))
        self.s_socket.listen(5)
        self.log = LogManager.get_logger()

        if self.log:
            self.log.log_info(
                'ServerConnection', '__init__', 'opening a server socket connection.')

    def accept_connection(self):
        """
            Description: Function to accept Connection from client side.

            Argument : None

            Return Type : None
        """
        while True:
            try:
                clientsocket, addr = self.s_socket.accept()
                print(addr)
                recv_data = clientsocket.recv(1024)
                response = self.process_request(recv_data)

                if self.log:
                    msg_string = 'sending a response object to client now.'
                    self.log.log_info(
                        'ServerConnection', 'accept_connection', msg_string)

                clientsocket.send(self.seralizer_object.serialize(response))

                if self.log:
                    msg_string = 'closing the socket connection.'
                    self.log.log_info(
                        'ServerConnection', 'accept_connection', msg_string)
            except Exception as error:
                raise Exception(error.__str__())
            finally:
                clientsocket.close()

    def process_request(self, recv_data):
        """
            Description: process request function processes the request object
            and its parameters, and return the response object. 
            It will take recv_data which represent the data coming from clinet
            as an argument.

            Argument : client_socket to access client socket object and 
            request_json to process the request data.

            Return Type : None
        """
        if self.log:
            self.log.log_info(
                'ServerConnection', 'process_request', 'a new request comes up.')

        if self.log:
            msg_string = 'serialization is going to happen now.'
            self.log.log_info(
                'ServerConnection', 'process_request', msg_string)

        self.seralizer_object = TDSSerializerFactory.get_serializer()
        request = self.seralizer_object.deserialize(recv_data)
        return_message = request.get_header('message')
        response = TDSResponse()  # TDS Response Object
        response.set_protocol_type('response')
        response.set_value("message", return_message[::-1])
        response.set_value("protocol_version", "1.0")
        response.set_value("protocol_format", "JSON")
        response.set_status("True")
        response.set_error_code(0)
        response.set_error_message("No Error")
        response.set_destination_ip(request.get_destination_ip())
        response.set_destination_port(request.get_destination_port())
        response.set_source_ip(self.h_name)
        response.set_source_port(self.p_number)
        print(response.__dict__)
        return response

s = ServerConnection()
s.accept_connection()
