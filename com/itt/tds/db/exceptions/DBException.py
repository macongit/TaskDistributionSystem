"""DBException Class"""


class DBException(Exception):

    """DBException Class"""

    def __init__(self, error_string, error_code=None):
        """Instantiate DBException class object"""
        super().__init__()
        self.error_string = error_string
        self.error_code = error_code

    def get_message(self):
        """Returning error message"""
        if self.error_code is None:
            return self.error_string
        else:
            return self.error_code + " : " + self.error_string
