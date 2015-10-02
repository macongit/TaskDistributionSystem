"""Client DAO Interface"""

try:
    from abc import abstractmethod

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'ClientDAO', 'Import Module', error.__str__(), str(error))


class ClientDAO:

    """@Interface"""
    @abstractmethod
    def add(self, client):
        """@ParamType client com.itt.tds.dao.ClientDAO
        @ReturnType int"""
        pass

    @abstractmethod
    def modify(self, client):
        """@ParamType client com.itt.tds.dao.ClientDAO
        @ReturnType void"""
        pass

    @abstractmethod
    def delete(self, client):
        """@ParamType client com.itt.tds.dao.ClientDAO
        @ReturnType void"""
        pass

    @abstractmethod
    def get_clients(self):
        """@ParamType client com.itt.tds.dao.ClientDAO
        @ReturnType void"""
        pass
