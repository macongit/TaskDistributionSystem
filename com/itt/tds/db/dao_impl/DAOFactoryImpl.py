"""DAO Factory Implementation"""

try:
    from com.itt.tds.db.dao.DAOFactory import DAOFactory
    from com.itt.tds.db.dao_impl.ClientDAOImpl import ClientDAOImpl
    from com.itt.tds.db.dao_impl.NodeDAOImpl import NodeDAOImpl
    from com.itt.tds.db.dao_impl.TaskInstanceDAOImpl import TaskInstanceDAOImpl

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'DAOFactoryImpl', 'Import Module', error.__str__(), str(error))


class DAOFactoryImpl(DAOFactory, object):

    """Implements DAOFactory interface, this implementation will return
    requested DAO Object"""
    __dao_factory_instance = None

    def __new__(cls):
        """Overriding __new__ to make a singleton DAO object"""
        if DAOFactoryImpl.__dao_factory_instance is None:
            return object.__new__(cls)
        else:
            return DAOFactoryImpl.__dao_factory_instance

    def __init__(self):
        """@ReturnType void"""
        if DAOFactoryImpl.__dao_factory_instance is None:
            DAOFactoryImpl.__dao_factory_instance = self
            self.object = None

    def get_dao(self, type_of_object):
        """Returning requested DAO Object"""
        if type_of_object == "Client":
            return self.get_client_dao()
        elif type_of_object == "Task":
            return self.get_task_instance_dao()
        elif type_of_object == "Node":
            return self.get_node_dao()

    def get_client_dao(self):
        """@ReturnType com.itt.tds.db.dao.ClientDAO"""
        self.object = ClientDAOImpl()
        return self.object

    def get_task_instance_dao(self):
        """@ReturnType com.itt.tds.db.dao.TaskInstanceDAO"""
        self.object = TaskInstanceDAOImpl()
        return self.object

    def get_node_dao(self):
        """@ReturnType com.itt.tds.db.dao.NodeDAO"""
        self.object = NodeDAOImpl()
        return self.object
