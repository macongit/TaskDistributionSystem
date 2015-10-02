"""Node class"""


class ProcessingNode:

    """Node class contains methods for store and retrieve node information"""

    def __init__(self):
        """initialization function for node object"""
        self._host_name = None
        self._port = None
        self._status = None
        self._node_id = None
        self._name = None
        self.current_task = None

    """
        def executeTask(self, taskInstance):
            @ParamType taskInstance tds.model.TaskInstance
                @ReturnType void
            pass
    """

    @property
    def port(self):
        """getting port for node object"""
        return self._port

    @port.setter
    def port(self, port):
        """setting port for node object"""
        self._port = port

    @property
    def host_name(self):
        """getting host name for node object"""
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Setting host name for node object"""
        self._host_name = host_name

    @property
    def name(self):
        """getting name for node object"""
        return self._name

    @name.setter
    def name(self, name):
        """Setting name for node object"""
        self._name = name

    @property
    def status(self):
        """getting status for node object"""
        return self._status

    @status.setter
    def status(self, status):
        """Setting status for node object"""
        self._status = status

    @property
    def node_id(self):
        """getting node id for node object"""
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Setting node id for node object"""
        self._node_id = node_id
