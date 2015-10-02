"""TaskAlreadyExistsException Class"""

try:
    from com.itt.tds.db.exceptions.RecordAlreadyExistsException import RecordAlreadyExistsException

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'TaskAlreadyExistsException', 'Import Module', error.__str__(), str(error))


class TaskAlreadyExistsException(RecordAlreadyExistsException):

    """TaskAlreadyExistsException"""

    def __init__(self, error_string, error_code=None):
        super().__init__(error_string, error_code)
