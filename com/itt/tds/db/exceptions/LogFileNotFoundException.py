"""Exception Class to handle the LogFile Not Found errors for TDS"""


class LogFileNotFoundException(Exception):

    """Exception Class to handle the configuration Not Found errors for TDS"""

    def __init__(self, error_string):
        """initialization of ConfigurationNotFoundException exception object"""
        super().__init__()
        self.error_string = error_string

    def get_message(self):
        print(self.error_string)
