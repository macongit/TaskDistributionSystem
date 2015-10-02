"""DBManager Interface"""

try:
    from abc import abstractmethod

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'DBManager', 'Import Module', error.__str__(), str(error))


class DBManager:

    """@Interface"""
    @abstractmethod
    def get_connection(self, connection_string):
        """needs to implement as DB Connection method"""
        pass

    @abstractmethod
    def close_connection(self):
        """needs to implement as DB Close method"""
        pass

    @abstractmethod
    def execute_dml_query(self, query, type_of_query):
        """needs to implement as query executor method"""
        pass

    @abstractmethod
    def execute_select_query(self, query):
        """needs to implement as query executor method"""
        pass
