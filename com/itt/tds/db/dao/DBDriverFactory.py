"""DB Driver Factory Interface"""

try:
    from abc import abstractmethod

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'DBDriverFactory', 'Import Module', error.__str__(), str(error))


class DBDriverFactory:

    """@Interface
    Driver Factory should create the instance of a request DB class and return
    the instance. Should be a singleton class."""

    @abstractmethod
    def get_db_driver(self, type_of_db):
        """@ReturnType com.itt.tds.db.dao.DBDriver"""
        pass
