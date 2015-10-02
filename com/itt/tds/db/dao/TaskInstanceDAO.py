"""TaskInstance DAO Interface"""

try:
    from abc import abstractmethod

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'TaskInstanceDAO', 'Import Module', error.__str__(), str(error))


class TaskInstanceDAO:

    """TaskInstance DAO Interface"""

    @abstractmethod
    def add(self, task_instance):
        """needs to implement to add new task instance"""
        pass

    @abstractmethod
    def delete(self, task_instance):
        """needs to implement to delete tasks"""
        pass

    @abstractmethod
    def modify(self, task_instance):
        """needs to implement to modify task details"""
        pass

    @abstractmethod
    def set_task_status(self, task_id, task_status):
        """needs to implement to set task status through task_id"""
        pass

    @abstractmethod
    def get_tasks_by_client_id(self, client_id):
        """needs to implement to return list of task objects of
        requested client_id"""
        pass

    @abstractmethod
    def get_task_by_id(self, task_id):
        """needs to implement to return task by its id value"""
        pass

    @abstractmethod
    def get_tasks_by_status(self, task_status):
        """needs to implement to return task by its status"""
        pass

    @abstractmethod
    def get_tasks_by_node_id(self, node_id):
        """needs to implement to return task by its node id value"""
        pass

    @abstractmethod
    def assign_node(self, node, task_instance):
        """needs to implement to assign a node for a task instance"""
        pass
