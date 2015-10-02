"""Node DAO Interface"""

try:
    from abc import abstractmethod

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'NodeDAO', 'Import Module', error.__str__(), str(error))


class NodeDAO:

    """Node DAO Interface"""
    @abstractmethod
    def add(self, node):
        """needs to implement to add a new node"""
        pass

    @abstractmethod
    def modify(self, node):
        """needs to implement to modify node"""
        pass

    @abstractmethod
    def delete(self, node):
        """needs to implement to delete node"""
        pass

    @abstractmethod
    def get_available_nodes(self):
        """needs to implement to return all
        available nodes in the form of list of node
        objects"""
        pass

    @abstractmethod
    def get_all_nodes(self):
        """needs to implement to return all
        nodes in the form of list of node
        objects"""
        pass
