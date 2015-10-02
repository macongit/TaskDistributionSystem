
from com.itt.tds.sockets.TDSProtocol import TDSProtocol


class TDSRequest(TDSProtocol):

    def __init__(self):
        super().__init__()

    def get_protocol_type(self):
        """
            Description : Function to get protocol type of request which sent
            to server.

            Return Type : It returns protocol_type of request object.
        """
        return self.request_type

    def set_protocol_type(self, request_type):
        """
            Description : Function to set protocol_type of request object
            which sent along with request.

            Return Type : None.
        """
        self.type = request_type

    def get_protocol_format(self):
        """
            Description : Function to get protocol type of request which sent
            to server.

            Return Type : It returns protocol_type of request object.
        """
        return self.protocol_format

    def set_protocol_format(self, protocol_format):
        """
            Description : Function to set protocol_type of request object
            which sent along with request.

            Return Type : None.
        """
        self.protocol_format = protocol_format

    def get_source_ip(self):
        """
            Description : Function to get the ip address of source node

            Return Type : It returns the ip adress of source node.
        """
        return self.source_ip

    def set_source_ip(self, source_ip):
        """
            Description : Function to set the ip address of source node.

            Return Type : None
        """
        self.source_ip = source_ip

    def get_source_port(self):
        """
            Description : Function to get port of source node.

            Return Type : It returns port of source node.
        """
        return self.source_port

    def set_source_port(self, port):
        """
            Description : Function to set port of source node.

            Return Type : None.
        """
        self.source_port = port

    def get_destination_ip(self):
        """
            Description : Function to get the ip address of destination node.

            Return Type : It returns ip address of destination node.
        """
        return self.dest_ip

    def set_destination_ip(self, destination_ip):
        """
            Description : Function to set the ip address of destination node.

            Return Type : None.
        """
        self.dest_ip = destination_ip

    def get_destination_port(self):
        """
            Description : Function to get the port address of destination node.

            Return Type : It returns port of destination node.
        """
        return self.dest_port

    def set_destination_port(self, port):
        """
            Description : Function to set the port address of destination node.

            Return Type : None.
        """
        self.dest_ip = port

    def get_method(self):
        """
            Description : Function to get request method from headers which sent along with
            request.

            Return Type : It returns headers of request object.
        """
        self.get_header("method")

    def set_method(self, method):
        """
            Description : Function to set method into request headers which sent along with
            request.

            Return Type : It returns headers of request object.
        """
        self.set_header("method", method)

    def get_header(self, header_key):
        """
            Description : Function to get request headers which sent along with
            request.

            Return Type : It returns headers of request object.
        """
        try:
            return self.headers[header_key]
        except KeyError as error:
            raise KeyError(error.__str__())

    def set_header(self, key, value):
        """
            Description : Function to set request headers which sent along with
            request.

            Return Type : None
        """
        self.headers[key] = value

    def get_parameter(self, key):
        """
            Description : Function to get request parameters of request object.

            Return Type : It returns the value of passed key as an argument.

            Arguments : It takes key as an argument and returns its value.
        """
        self.get_header(key)

    def add_parameter(self, key, value):
        """
            Description : Function to set value of a key in request object.

            Return Type : None
        """
        self.set_header(key, value)
