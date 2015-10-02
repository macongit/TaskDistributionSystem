
try:
    import unittest
    from com.itt.tds.db.dao_impl.TaskInstanceDAOImpl import TaskInstanceDAOImpl
    from com.itt.tds.model.TaskInstance import TaskInstance
    from com.itt.tds.db.exceptions.TaskAlreadyExistsException import TaskAlreadyExistsException
    from com.itt.tds.db.exceptions.TaskNotFoundException import TaskNotFoundException

except ImportError as error:
    print(error.__str__())
    from com.itt.tds.logs.LogManager import LogManager
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'TaskInstanceUnitTest', 'Import Module', error.__str__(), str(error))


class TaskInstanceUnitTest(unittest.TestCase):
    _task_dao = TaskInstanceDAOImpl()

    def setUp(self):
        """Initialization method for test cases which will run for each test 
        case"""
        self.test_data = self.read_data('test_data/tasks.txt')

    def read_data(self, file_name):
        """Function is responsible for reading the given file and return the file
        data as dictionary
            Passing Arguments:
            file_name : Represents a file name which needs to be read

            Return Value:
            dictionary : Returns a dictionary type of object which stores the file 
            data as per line basis
        """
        test_data_dict = {}
        i = 0
        file_handler = open(file_name)
        for data in file_handler.readlines():
            if i == 0:
                pass
            else:
                if data[len(data) - 1] == '\n':
                    data = data[:len(data) - 1]
                test_data_dict[i] = data
            i += 1
        file_handler.close()
        return test_data_dict

#    @unittest.skip("task addition step")
    def test_01_add_task(self):
        """
        Test case for adding new tasks into the database.It is useful for 
        testing the functionality of 
        TaskInstance's add method."""
        try:
            for k, v in self.test_data.items():
                task_instance = TaskInstance()
                test_str = v.split(',')
                task_instance.task_id = test_str[0]
                task_instance.client_id = test_str[1]
                task_instance.node_id = test_str[2]
                task_instance.task_name = test_str[3]
                task_instance.task_parameters = test_str[4]
                task_instance.task_exe_path = test_str[5]
                task_instance.task_state = test_str[6]
                task_instance.task_status = test_str[7]
                task_instance.task_result = test_str[8]
                task_instance.task_error_message = test_str[9]
                TaskInstanceUnitTest._task_dao.add(task_instance)
                self.assertTrue(TaskInstanceUnitTest._task_dao.get_task_by_id(test_str[0]))

            for k, v in self.test_data.items():
                task_instance = TaskInstance()
                test_str = v.split(',')
                task_instance.task_id = test_str[0]
                self.assertTrue(
                    TaskInstanceUnitTest._task_dao.delete(task_instance))

        except DBException as error:
            print(error.get_message())

    @unittest.skip("Task modify step")
    def test_02_update_task(self):
        """
        Test case for updating tasks into the database.It is useful for 
        testing the functionality of 
        TaskInstance's modify method."""
        for k, v in self.test_data.items():
                task_instance = TaskInstance()
                test_str = v.split(',')
                task_instance.task_id = test_str[0]
                task_instance.client_id = test_str[1]
                task_instance.node_id = test_str[2]
                task_instance.task_name = test_str[3]
                task_instance.task_parameters = test_str[4]
                task_instance.task_exe_path = test_str[5]
                task_instance.task_state = test_str[6]
                task_instance.task_status = test_str[7]
                task_instance.task_result = test_str[8]
                task_instance.task_error_message = test_str[9]
                TaskInstanceUnitTest._task_dao.add(task_instance)
                self.assertTrue(TaskInstanceUnitTest._task_dao.get_task_by_id(test_str[0]))

        for k, v in self.test_data.items():
            task_instance = TaskInstance()
            test_str = v.split(',')
            task_instance.task_id = test_str[0]
            task_instance.client_id = test_str[1]
            task_instance.node_id = test_str[2]
            task_instance.task_name = test_str[3]
            task_instance.task_parameters = test_str[4]
            task_instance.task_exe_path = test_str[5]
            task_instance.task_state = test_str[6]
            task_instance.task_status = test_str[7]
            task_instance.task_result = test_str[8]
            task_instance.task_error_message = test_str[9]
            TaskInstanceUnitTest._task_dao.modify(task_instance)

    @unittest.skip("set task status step")
    def test_03_set_task_status(self):
        """
        Test case for setting a task status into the database for example 
        success/failure/error etc."""
        for k, v in self.test_data.items():
            test_str = v.split(',')
            self.assertTrue(
                TaskInstanceUnitTest._task_dao.set_task_status(test_str[0], 'success'))

    @unittest.skip("set task status step")
    def test_05_set_task_status_exception(self):
        """
        Test case for setting a task status into the database for example 
        success/failure/error etc. It should throw an exception if passed 
        task id is not in database."""
        try:
            for k, v in self.test_data.items():
                self.assertTrue(
                    TaskInstanceUnitTest._task_dao.set_task_status(100, 'success'))

        except TaskNotFoundException as error:
            print(error.__str__())

    @unittest.skip("get tasks by client id step")
    def test_05_get_tasks_by_client_id(self):
        """
        Test case for retrieving the tasks based on client id. It is validating
        that system contains tasks for specific client or not."""
        for k, v in self.test_data.items():
            test_str = v.split(',')
            client_id = 1
            self.assertGreaterEqual(
                len(TaskInstanceUnitTest._task_dao.get_tasks_by_client_id(client_id)), 0)

    @unittest.skip("get tasks by client id step")
    def test_06_get_tasks_by_client_id_exception(self):
        """
        Test case for retrieving the tasks based on client id. It is validating
        that system contains tasks for specific client or not.It should throw 
        an exception if passed 
        client id is not in database."""
        try:
            for k, v in self.test_data.items():
                test_str = v.split(',')
                client_id = 100
                self.assertGreaterEqual(
                    len(TaskInstanceUnitTest._task_dao.get_tasks_by_client_id(client_id)), 0)

        except TaskNotFoundException as error:
            print(error.__str__())

    @unittest.skip("get task by id step")
    def test_07_get_task_by_id(self):
        """
        Test case for retrieving the tasks based on its id. """
        for k, v in self.test_data.items():
            test_str = v.split(',')
            task_id = test_str[0]
            self.assertTrue(
                TaskInstanceUnitTest._task_dao.get_task_by_id(task_id))

    @unittest.skip("get task by id step")
    def test_08_get_task_by_id_exception(self):
        """
        Test case for retrieving the tasks based on its id. It should throw 
        an exception if passed 
        task id is not in database."""
        try:
            for k, v in self.test_data.items():
                test_str = v.split(',')
                """ task_id = test_str[0] """
                task_id = 200  # custom argument
                self.assertTrue(
                    TaskInstanceUnitTest._task_dao.get_task_by_id(task_id))

        except TaskNotFoundException as error:
            print(error.__str__())

    @unittest.skip("get task by status step")
    def test_09_get_tasks_by_status(self):
        """
        Test case for retrieving the tasks based on the current task status. It
        validates the retuning output matches with the given task status input or not."""
        for k, v in self.test_data.items():
            test_str = v.split(',')
            task_status = test_str[7]
            self.assertGreaterEqual(
                len(TaskInstanceUnitTest._task_dao.get_tasks_by_status(task_status)), 0)

    @unittest.skip("get task by status step")
    def test_10_get_tasks_by_status_exception(self):
        """
        Test case for retrieving the tasks based on the current task status. It
        validates the retuning output matches with the given task status input 
        or not.It should throw an exception if passed 
        task status is not a type of value to the database field."""
        try:
            for k, v in self.test_data.items():
                test_str = v.split(',')
                """task_status = test_str[7]"""
                task_status = str(3)
                self.assertGreaterEqual(
                    len(TaskInstanceUnitTest._task_dao.get_tasks_by_status(task_status)), 0)

        except TaskNotFoundException as error:
            print(error.__str__())

    @unittest.skip("get task by node id step")
    def test_11_get_tasks_by_node_id(self):
        """
        Test case for retrieving the tasks based on node id. It is validating that
        how many tasks are there for a specific node which is pending for execution."""
        for k, v in self.test_data.items():
            test_str = v.split(',')
            """node_id = test_str[2]"""
            node_id = 1
            self.assertGreaterEqual(
                len(TaskInstanceUnitTest._task_dao.get_tasks_by_node_id(node_id)), 0)

    @unittest.skip("get task by node id step")
    def test_12_get_tasks_by_node_id_exception(self):
        """
        Test case for retrieving the tasks based on node id. It is validating that
        how many tasks are there for a specific node which is pending for 
        execution. It should throw an exception if passed 
        node id is not in database."""
        try:
            for k, v in self.test_data.items():
                test_str = v.split(',')
                """node_id = test_str[2]"""
                node_id = 100
                self.assertGreaterEqual(
                    len(TaskInstanceUnitTest._task_dao.get_tasks_by_node_id(node_id)), 0)

        except TaskNotFoundException as error:
            print(error.__str__())

    @unittest.skip("Task deletion step")
    def test_13_delete_task(self):
        """
        Test case for deleting tasks from the database.It is useful 
        for testing the functionality of 
        TaskInstance's add method."""
        for k, v in self.test_data.items():
            task_instance = TaskInstance()
            test_str = v.split(',')
            task_instance.task_id = test_str[0]
            self.assertTrue(
                TaskInstanceUnitTest._task_dao.delete(task_instance))

    @unittest.skip("Task deletion step")
    def test_14_update_task_exception(self):
        """
        Test case for updating tasks into the database.It is useful for 
        testing the functionality of 
        TaskInstance's modify method. It should throw an exception because it is
        updating the tasks which are not in database."""
        try:
            for k, v in self.test_data.items():
                task_instance = TaskInstance()
                test_str = v.split(',')
                task_instance.task_id = test_str[0]
                task_instance.client_id = test_str[1]
                task_instance.node_id = test_str[2]
                task_instance.task_name = test_str[3]
                task_instance.task_parameters = test_str[4]
                task_instance.task_exe_path = test_str[5]
                task_instance.task_state = test_str[6]
                task_instance.task_status = test_str[7]
                task_instance.task_result = test_str[8]
                task_instance.task_error_message = test_str[9]
                self.assertTrue(
                    TaskInstanceUnitTest._task_dao.modify(task_instance))

        except TaskNotFoundException as error:
            print(error.__str__())

    def tearDown(self):
        return None

if __name__ == '__main__':
    unittest.main()
