""" DAO Factory Interface"""
try:
    from abc import abstractmethod

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'DAOFactory', 'Import Module', error.__str__(), str(error))


class DAOFactory:

    """@Interface
    DAO Factory should create the instance of a request
    DAO class and return the instance. Should be a singleton class."""
    @abstractmethod
    def get_client_dao(self):
        """@ReturnType com.itt.tds.db.dao.ClientDAO"""
        pass

    @abstractmethod
    def get_task_instance_dao(self):
        """@ReturnType com.itt.tds.db.dao.TaskInstanceDAO"""
        pass

    @abstractmethod
    def get_node_dao(self):
        """@ReturnType com.itt.tds.db.dao.NodeDAO"""
        pass
