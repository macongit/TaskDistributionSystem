"""DBConnectionException Class"""

try:
    from com.itt.tds.db.exceptions.DBException import DBException

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'DBConnectionException', 'Import Module', error.__str__(), str(error))


class DBConnectionException(DBException):

    """DBConnectionException Class"""

    def __init__(self, error_string, error_code=None):
        """Instantiate DBConnectionException class object"""
        super().__init__(error_string, error_code)
