"""TaskInstanceDAO Implementation"""

try:
    import mysql.connector
    import re
    from com.itt.tds.db.dao.TaskInstanceDAO import TaskInstanceDAO
    from com.itt.tds.db.dao_impl.DBDriverFactoryImpl import DBDriverFactoryImpl
    from com.itt.tds.cfg.TDSConfiguration import TDSConfiguration
    from com.itt.tds.logs.LogManager import LogManager
    from com.itt.tds.model.TaskInstance import TaskInstance
    from com.itt.tds.db.exceptions.TaskAlreadyExistsException import TaskAlreadyExistsException
    from com.itt.tds.db.exceptions.TaskNotFoundException import TaskNotFoundException
    from com.itt.tds.db.exceptions.DBException import DBException

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'TaskInstanceDAOImpl', 'Import Module', error.__str__(), str(error))


class TaskInstanceDAOImpl(TaskInstanceDAO):

    """TaskInstanceDAO Implementation"""

    def __init__(self):
        self.db_manager = DBDriverFactoryImpl().get_db_driver(
            TDSConfiguration().db_type)
        self.log = LogManager.get_logger()

    def add(self, task_instance):
        """Adding a new task into the system"""
        try:
            task_query = "INSERT into Task (id,taskName,taskExePath) values ('" + task_instance.task_id + \
                "','" + task_instance.task_name + "','" + \
                re.escape(task_instance.task_exe_path) + "')"
            if self.log:
                self.log.log_debug('TaskInstanceDAOImpl', 'add', task_query)
            self.db_manager.execute_dml_query(task_query, "Insert")

        except mysql.connector.IntegrityError as error:
            if self.log:
                self.log.log_debug(
                    'TaskInstanceDAOImpl', 'add', error.__str__())

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'add', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        try:
            task_instance.client_id = 1  # to be removed
            task_instance.node_id = 1  # to be removed
            task_instance_query = "INSERT into TaskInstance (taskStates,taskParameters,taskStatus,taskErrorMessage,taskResult,Client_id,Node_id,Task_id) values ( " + str(task_instance.task_state) + ", " + task_instance.task_parameters + \
                ", " + task_instance.task_status + ", " + task_instance.task_error_message + ", " + task_instance.task_result + \
                ", " + str(task_instance.client_id) + ", " + \
                str(task_instance.node_id) + ", " + \
                str(task_instance.task_id) + ")"
            if self.log:
                self.log.log_debug(
                    'TaskInstanceDAOImpl', 'add', task_instance_query)
            self.db_manager.execute_dml_query(
                task_instance_query, "Insert")
            if self.log:
                self.log.log_info(
                    'TaskInstanceDAOImpl', 'add', "A new task with task id " + str(task_instance.task_id) +
                                                  " has been added")
            return True

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'add', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        finally:
            self.db_manager.close_connection()

    def delete(self, task_instance):
        """Deleting a task from the system"""
        try:
            query = "SELECT id from Task where id = '" + \
                str(task_instance.task_id) + "'"
            if self.log:
                self.log.log_debug('TaskInstanceDAOImpl', 'delete', query)
            row_id = self.db_manager.execute_select_query(query)
            if not row_id:
                raise TaskNotFoundException(
                    'task with task id ' + str(task_instance.task_id) + ' does not exists.')
            else:
                task_instance_query = "delete from TaskInstance where Task_id = '" + \
                    str(task_instance.task_id) + "'"
                task_query = "delete from Task where id = '" + \
                    str(task_instance.task_id) + "'"
                if self.log:
                    self.log.log_debug(
                        'TaskInstanceDAOImpl', 'delete', task_instance_query)
                self.db_manager.execute_dml_query(
                    task_instance_query, "Delete")
                if self.log:
                    self.log.log_debug(
                        'TaskInstanceDAOImpl', 'delete', task_query)
                self.db_manager.execute_dml_query(task_query, "Delete")
                if self.log:
                    self.log.log_info('TaskInstanceDAOImpl', 'delete', "A task with task id " + str(
                        task_instance.task_id) + " has been deleted.")
                return True

        except TaskNotFoundException as error:
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'delete', error.get_message(), 'TaskNotFoundException')
            raise TaskNotFoundException(error.get_message())

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'delete', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        finally:
            self.db_manager.close_connection()

    def modify(self, task_instance):
        """Modify the existing task details into system"""
        try:
            query = "SELECT id from Task where id = '" + \
                str(task_instance.task_id) + "'"
            if self.log:
                self.log.log_debug('TaskInstanceDAOImpl', 'modify', query)
            row_id = self.db_manager.execute_select_query(query)
            if not row_id:
                raise TaskNotFoundException(
                    'task with task id ' + str(task_instance.task_id) + ' does not exists.')
            else:
                task_query = "Update Task set taskName = '" + str(task_instance.task_name) + "', taskExePath = '" + str(
                    task_instance.task_exe_path) + "' where id = '" + str(task_instance.task_id) + "'"

                task_instance.node_id = 1  # to be removed
                task_instance.client_id = 1  # to be removed
                task_instance_query = "Update TaskInstance set taskStates = '" + str(task_instance.task_state) + "', taskStatus = '" + str(task_instance.task_status) + "', taskErrorMessage = '" + task_instance.task_error_message + "', taskResult = '" + \
                    task_instance.task_result + "', taskParameters = '" + task_instance.task_parameters + "', Client_id = '" + \
                    str(task_instance.client_id) + "', Node_id = '" + str(task_instance.node_id) + \
                    "' where Task_id = '" + str(task_instance.task_id) + "'"
                if self.log:
                    self.log.log_debug(
                        'TaskInstanceDAOImpl', 'modify', task_query)
                    self.log.log_debug(
                        'TaskInstanceDAOImpl', 'modify', task_instance_query)

                self.db_manager.execute_dml_query(task_query, "Update")
                self.db_manager.execute_dml_query(
                    task_instance_query, "Update")
                return True

        except TaskNotFoundException as error:
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'modify', error.get_message(), 'TaskNotFoundException')
            raise TaskNotFoundException(error.get_message())

        except mysql.connector.IntegrityError as error:
            error_code = error.__str__().split(':')[0]
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'modify', error.__str__(), 'TaskAlreadyExistsException')
            raise TaskAlreadyExistsException(
                "Task is not updates due to " + str(task_instance.task_exe_path), error_code)

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'modify', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        finally:
            self.db_manager.close_connection()

    def set_task_status(self, task_id, task_status):
        """Setting task status"""
        try:
            query = "SELECT id from TaskInstance where Task_id = '" + \
                str(task_id) + "'"
            if self.log:
                self.log.log_debug(
                    'TaskInstanceDAOImpl', 'set_task_status', query)
            row_id = self.db_manager.execute_select_query(query)
            if not row_id:
                raise TaskNotFoundException(
                    'task with task id ' + str(task_id) + ' does not exists.')
            else:
                task_instance_update_query = "Update TaskInstance set taskStatus = '" + \
                    task_status + "' where Task_id = " + str(task_id)
                if self.log:
                    self.log.log_debug(
                        'TaskInstanceDAOImpl', 'set_task_status',  task_instance_update_query)
                self.db_manager.execute_dml_query(task_instance_update_query)
                return True

        except TaskNotFoundException as error:
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'set_task_status', error.get_message(), 'TaskNotFoundException')
            raise TaskNotFoundException(error.get_message())

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'set_task_status', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        finally:
            self.db_manager.close_connection()

    def get_tasks_by_client_id(self, client_id):
        """retrieving tasks for specific client"""
        try:
            query = "SELECT Task_id from TaskInstance where Client_id = '" + \
                str(client_id) + "'"
            if self.log:
                self.log.log_debug(
                    'TaskInstanceDAOImpl', 'get_tasks_by_client_id', query)
            task_ids = self.db_manager.execute_select_query(query)
            if not task_ids:
                raise TaskNotFoundException(
                    'Task for client id ' + str(client_id) + ' does not exists.')

        except TaskNotFoundException as error:
            if self.log:
                self.log.log_error('TaskInstanceDAOImpl', 'get_tasks_by_client_id', error.get_message(
                ), 'TaskNotFoundException')
            raise TaskNotFoundException(error.get_message())

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'get_tasks_by_client_id', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        else:
            list_of_tasks = []
            for task_id in task_ids:
                row = self.db_manager.execute_select_query(
                    "SELECT id,taskName,taskExePath from Task where id = '" + str(task_id) + "'")
                if row:
                    task_object = TaskInstance()
                    task_object.task_id = row[0]
                    task_object.task_name = row[1]
                    task_object.task_exe_path = row[2]
                    list_of_tasks.append(task_object)

            return list_of_tasks

        finally:
            self.db_manager.close_connection()

    def get_task_by_id(self, task_id):
        """retrieving task for given task id"""
        try:
            query = "SELECT id,taskName,taskExePath from Task where id = '" + \
                str(task_id) + "'"
            if self.log:
                self.log.log_debug(
                    'TaskInstanceDAOImpl', 'get_task_by_id', query)
            row = self.db_manager.execute_select_query(query)
            if not row:
                raise TaskNotFoundException(
                    'No Task has been created yet for task id ' + str(task_id))

        except TaskNotFoundException as error:
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'get_task_by_id', error.get_message(), 'TaskNotFoundException')
            raise TaskNotFoundException(error.get_message())

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'get_task_by_id', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        else:
            task_object = TaskInstance()
            task_object.task_id = row[0][0]
            task_object.task_name = row[0][1]
            task_object.task_exe_path = row[0][2]

            return task_object

        finally:
            self.db_manager.close_connection()

    def get_tasks_by_status(self, task_status):
        """retrieving task for given task status"""
        try:
            query = "SELECT Task_id from TaskInstance where taskStatus = " + \
                task_status + ""
            if self.log:
                self.log.log_debug(
                    'TaskInstanceDAOImpl', 'get_tasks_by_status', query)
            task_ids = self.db_manager.execute_select_query(query)
            if not task_ids:
                raise TaskNotFoundException(
                    'Task does not exists yet for tasks status ' + str(task_status))

        except TaskNotFoundException as error:
            if self.log:
                self.log.log_error('TaskInstanceDAOImpl', 'get_tasks_by_status', error.get_message(
                ), 'TaskNotFoundException')
            raise TaskNotFoundException(error.get_message())

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'get_task_by_status', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        else:
            list_of_tasks = []
            for task_id in task_ids:
                row = self.db_manager.execute_select_query(
                    "SELECT id,taskName,taskExePath from Task where id = '" + str(task_id) + "'")
                if row:
                    task_object = TaskInstance()
                    task_object.task_id = row[0]
                    task_object.task_name = row[1]
                    task_object.task_exe_path = row[2]
                    list_of_tasks.append(task_object)

            return list_of_tasks

        finally:
            self.db_manager.close_connection()

    def get_tasks_by_node_id(self, node_id):
        """retrieving tasks for given node id"""
        try:
            query = "SELECT Task_id from TaskInstance where Node_id = '" + \
                str(node_id) + "'"
            if self.log:
                self.log.log_debug(
                    'TaskInstanceDAOImpl', 'get_tasks_by_node_id', query)
            task_ids = self.db_manager.execute_select_query(query)
            if not task_ids:
                raise TaskNotFoundException(
                    'No tasks has been assigned to node ' + str(node_id))

        except TaskNotFoundException as error:
            if self.log:
                self.log.log_error('TaskInstanceDAOImpl', 'get_tasks_by_node_id', error.get_message(
                ), 'TaskNotFoundException')
            raise TaskNotFoundException(error.get_message())

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'TaskInstanceDAOImpl', 'get_tasks_by_node_id', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        else:
            list_of_tasks = []
            for task_id in task_ids:
                row = self.db_manager.execute_select_query(
                    "SELECT id,taskName,taskExePath from Task where id = '" + str(task_id) + "'")
                if row:
                    task_object = TaskInstance()
                    task_object.task_id = row[0]
                    task_object.task_name = row[1]
                    task_object.task_exe_path = row[2]
                    list_of_tasks.append(task_object)

            return list_of_tasks

        finally:
            self.db_manager.close_connection()

    """
        def assign_node(self, node, task_instance):
            return
    """
