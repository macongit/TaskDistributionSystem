
try:
    import socket
    from com.itt.tds.comm.TDSRequest import TDSRequest
    from com.itt.tds.comm.TDSResponse import TDSResponse
    from com.itt.tds.comm.TDSSerializerFactory import TDSSerializerFactory
    from com.itt.tds.logs.LogManager import LogManager

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'ClientConnection', 'Import Module', error.__str__(), str(error))


class ClientConnection:

    def __init__(self):
        """
            Description: Initialization function for Client Connection Class

            Argument : None

            Return Type : None
        """
        self.c_socket = None
        self.log = LogManager.get_logger()

    def get_connection(self):
        """
            Description: Function to establish a connection to the server

            Argument : None

            Return Type : None
        """
        self.c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.h_name = socket.gethostname()
        self.server_p_number = 9994

        if self.log:
            self.log.log_info(
                'ClientConnection', '__init__', 'opening a client socket connection.')

        self.c_socket.connect((self.h_name, self.server_p_number))

    def send_data(self):
        """
            Description: Function to send data to the server in json format.
            For this purpose it creates a object of TDSRequest object and 
            converts the object in JSON format.

            Argument : None

            Return Type : None
        """
        msg = input('Enter message to server : ')
        request = TDSRequest()
        request.set_method("node-add")
        request.set_protocol_type('request')
        request.add_parameter("protocol_version", "1.0")
        request.add_parameter("node-name", "samplenode")
        request.add_parameter("node-ip", "192.168.2.52")
        request.add_parameter("node-port", "1000")
        request.add_parameter("protocol_format", "JSON")
        request.add_parameter("message", msg)
        request.set_destination_ip(self.h_name)
        request.set_destination_port(self.server_p_number)
        request.set_source_ip(self.h_name)

        if self.log:
            self.log.log_info(
                'ClientConnection', 'send_data', 'sending a request object to server.')

        self.seralizer_object = TDSSerializerFactory.get_serializer()
        self.c_socket.send(self.seralizer_object.serialize(request))

    def recv_data(self):
        """
            Description: Function to receive data from server in bytes 
            format and converts it into response object

            Argument : None

            Return Type : None
        """

        if self.log:
            self.log.log_info(
                'ClientConnection', 'recv_data', 'received a response object.')

        response_bytes = self.c_socket.recv(1024)
        response = self.seralizer_object.deserialize(response_bytes)
        print("Response Status : " + response.get_status())
        print("Response Error Message : " + response.get_error_message())
        print("Response Message : " + response.get_value('message'))

    def close_connection(self):
        """
            Description : Function to close the socket connection from server. 

            Argument : None

            Return Type : None
        """
        if self.log:
            msg_string = 'closing a socket connection at client side.'
            self.log.log_info(
                'ClientConnection', 'close_connection', msg_string)

        self.c_socket.close()

# calling ClientConnection
c = ClientConnection()
char = 'Y'
while char == 'Y':
    c.get_connection()
    c.send_data()
    c.recv_data()
    c.close_connection()
    char = input('Do you want to send more data (Y/N):  ')
