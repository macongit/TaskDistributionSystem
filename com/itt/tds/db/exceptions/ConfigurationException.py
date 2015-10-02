"""Exception Class to handle the configuration errors for TDS"""


class ConfigurationException(Exception):

    """Exception Class to handle the configuration errors for TDS"""

    def __init__(self, error_string):
        """initialization of ConfigurationException exception object"""
        super().__init__()
        self.error_string = error_string

    def get_message(self):
        """Displaying the error message string"""
        return self.error_string
