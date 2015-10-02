"""TaskInstance class"""


class TaskInstance:

    """TaskInstance class contains methods for store and retrieve
    Task information"""

    def __init__(self):
        """initialization function for Task Instance object"""
        self._task_name = None
        self._task_parameters = None
        self._task_exe_path = None
        self._task_state = None
        self._task_status = None
        self._task_result = None
        self._error_message = None
        self._task_id = None

    @property
    def task_name(self):
        """getting task name"""
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """setting task name"""
        self._task_name = task_name

    @property
    def task_exe_path(self):
        """getting task execution path"""
        return self._task_exe_path

    @task_exe_path.setter
    def task_exe_path(self, task_exe_path):
        """setting task execution path"""
        self._task_exe_path = task_exe_path

    @property
    def task_state(self):
        """getting task state"""
        return self._task_state

    @task_state.setter
    def task_state(self, task_state):
        """setting task state"""
        self._task_state = task_state

    @property
    def task_result(self):
        """getting task result"""
        return self._task_result

    @task_result.setter
    def task_result(self, task_result):
        """setting task result"""
        self._task_result = task_result

    @property
    def error_message(self):
        """getting error message"""
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """setting error message"""
        self._error_message = error_message

    @property
    def task_id(self):
        """@Returning Task id"""
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """setting task id"""
        self._task_id = task_id
