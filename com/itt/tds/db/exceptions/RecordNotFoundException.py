"""RecordNotFoundException Class"""

try:
    from com.itt.tds.db.exceptions.DBException import DBException

except ImportError as error:
    print(error.__str__())
    if log:
        log.log_warn(
            'RecordNotFoundException', 'Import Module', error.__str__(), str(error))


class RecordNotFoundException(DBException):

    """RecordNotFoundException Class"""

    def __init__(self, error_string, error_code=None):
        super().__init__(error_string, error_code)
