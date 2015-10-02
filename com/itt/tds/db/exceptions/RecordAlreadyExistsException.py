"""RecordAlreadyExistsException Class"""

try:
    from com.itt.tds.db.exceptions.DBException import DBException

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'RecordAlreadyExistsException', 'Import Module', error.__str__(), str(error))


class RecordAlreadyExistsException(DBException):

    """RecordAlreadyExistsException Class"""

    def __init__(self, error_string, error_code=None):
        """Instantiate RecordAlreadyExistsException class object"""
        super().__init__(error_string, error_code)
