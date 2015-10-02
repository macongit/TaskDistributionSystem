
from com.itt.tds.sockets.TDSProtocol import TDSProtocol


class TDSResponse(TDSProtocol):

    def __init__(self):
        super().__init__()

    def get_protocol_type(self):
        """
            Description : Function to get protocol type of response which sent
            to client.

            Return Type : It returns protocol_type of response object.
        """
        return self.request_type

    def set_protocol_type(self, request_type):
        """
            Description : Function to set protocol_type of response object
            which sent along with response.

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
        return self.destination_ip

    def set_destination_ip(self, destination_ip):
        """
            Description : Function to set the ip address of destination node.

            Return Type : None.
        """
        self.destination_ip = destination_ip

    def get_destination_port(self):
        """
            Description : Function to get the port address of destination node.

            Return Type : It returns port of destination node.
        """
        return self.destination_port

    def set_destination_port(self, port):
        """
            Description : Function to set the port address of destination node.

            Return Type : None.
        """
        self.destination_port = port

    def get_status(self):
        """
            Description : Function to get status from response object.

            Return Type : It returns a status value of response object.
        """
        return self.get_header('status')

    def set_status(self, status):
        """
            Description : Function to get status from response object.

            Return Type : None.
        """
        self.set_header('status', status)

    def get_error_code(self):
        """
            Description : Function to get error_code from response object.

            Return Type : It returns a error_code value of response object.
        """
        return self.get_header('error_code')

    def set_error_code(self, error_code):
        """
            Description : Function to get error_code from response object.

            Return Type : None.
        """
        self.set_header('error_code', error_code)

    def get_error_message(self):
        """
            Description : Function to get error_message from response object.

            Return Type : It returns a error_message value of response object.
        """
        return self.get_header('error_message')

    def set_error_message(self, error_message):
        """
            Description : Function to get error_message from response object.

            Return Type : None.
        """
        self.set_header('error_message', error_message)

    def get_header(self, key):
        """
            Description : Function to get value of key from response object.

            Return Type : It returns a value of a key from response object.
        """
        try:
            return self.headers[key]
        except KeyError as error:
            raise KeyError(error.__str__())

    def set_header(self, key, value):
        """
            Description : Function to set value for a key in response object.

            Return Type : None
        """
        self.headers[key] = value

    def set_value(self, key, value):
        """
            Description : Function to set value for a key in response object.

            Return Type : None
        """
        self.set_header(key, value)

    def get_value(self):
        """
            Description : Function to set value for a key in response object.

            Return Type : None
        """
        return self.get_header(key)
