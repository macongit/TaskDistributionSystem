
class TDSProtocol:

    def __init__(self):
        self.protocol_type = None
        self.source_ip = None
        self.dest_ip = None
        self.source_port = None
        self.dest_port = None
        self.headers = {}

    def get_header(self, header_key):
        pass

    def set_header(self, header_key, value):
        pass
