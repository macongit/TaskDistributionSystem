"""NodeAlreadyExistsException Class"""

try:
    from com.itt.tds.db.exceptions.RecordAlreadyExistsException import RecordAlreadyExistsException

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'NodeAlreadyExistsException', 'Import Module', error.__str__(), str(error))


class NodeAlreadyExistsException(RecordAlreadyExistsException):

    """NodeAlreadyExistsException"""

    def __init__(self, error_string, error_code=None):
        super().__init__(error_string, error_code)
