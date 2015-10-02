"""Application main module"""

try:
    import inspect
    from com.itt.tds.model.Client import Client
    from com.itt.tds.model.ProcessingNode import ProcessingNode
    from com.itt.tds.model.TaskInstance import TaskInstance
    from com.itt.tds.logs.LogManager import LogManager
    from com.itt.tds.db.dao_impl.DAOFactoryImpl import DAOFactoryImpl
    from com.itt.tds.db.exceptions.DBException import DBException
    from com.itt.tds.db.exceptions.ClientAlreadyExistsException import ClientAlreadyExistsException
    from com.itt.tds.db.exceptions.ClientNotFoundException import ClientNotFoundException
    from com.itt.tds.db.exceptions.NodeAlreadyExistsException import NodeAlreadyExistsException
    from com.itt.tds.db.exceptions.NodeNotFoundException import NodeNotFoundException
    from com.itt.tds.db.exceptions.TaskAlreadyExistsException import TaskAlreadyExistsException
    from com.itt.tds.db.exceptions.TaskNotFoundException import TaskNotFoundException
    from com.itt.tds.db.exceptions.DBConnectionException import DBConnectionException
    from com.itt.tds.db.exceptions.ConfigurationNotFoundException import ConfigurationNotFoundException

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'Main', 'Import Module', error.__str__(), str(error))


class Main:

    """Application main module"""

    def __init__(self):
        """Initialization method for Main object"""
        self.client = Client()
        self.node = ProcessingNode()
        self.task_instance = TaskInstance()
        try:
            self.log = LogManager.get_logger()
            self.client_dao = DAOFactoryImpl().get_dao('Client')
            self.node_dao = DAOFactoryImpl().get_dao('Node')
            self.task_dao = DAOFactoryImpl().get_dao('Task')

        except ConfigurationNotFoundException as error:
            frm = inspect.trace()[-1]
            mod = inspect.getmodule(frm[0])
            print(error.get_message())
            if "TDSConfiguration" in mod.__name__:
                exit(1)

        except ConfigurationLoadException as error:
            print(error.get_message())

    def get_input(self, type_of_input):
        """Seeking for input from client"""
        if type_of_input is 'initial':
            print("1. Client Operations.")
            print("2. Node Operations.")
            print("3. Task Operations.")
            print("4. Quit")

        elif type_of_input is 'next':
            print("1. New.")
            print("2. Update.")
            print("3. Delete.")
            print("4. List.")

        try:
            input_for_operation = int(
                input("Press choose corresponding number to process : "))
            if input_for_operation not in (1, 2, 3, 4):
                raise ValueError("Please enter integer from given range")

        except TypeError as error:
            if self.log:
                self.log.log_warn(
                    'Main', 'get_input', error.__str__(), 'TypeError')
            print(error.__str__())
            input_for_initial = self.get_input('initial')
            if input_for_initial is 4:
                log = LogManager.get_logger()
                if log:
                    log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                    if not log.file_object.closed:
                        print("bye world")
                        log.file_object.close()
                print("Bye")
                exit(1)

        except ValueError as error:
            if self.log:
                self.log.log_warn(
                    'Main', 'get_input', error.__str__(), 'ValueError')
            print(error.__str__())
            input_for_initial = self.get_input('initial')
            if input_for_initial is 4:
                log = LogManager.get_logger()
                if log:
                    log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")
                exit(1)

        except Exception:
            print("Quitting")
            exit(1)

        else:
            return input_for_operation

    def set_client(self, type_of_operation):
        """Seeking for input from user"""
        if type_of_operation in ("save", "update"):
            user_id = input("Enter userid : ")
            user_name = input("Enter username: ")
            host_name = input("Enter hostname : ")
            self.client.user_name = user_name
            self.client.user_id = user_id
            self.client.host_name = host_name

        elif type_of_operation == "delete":
            user_id = input("Enter userid : ")
            self.client.user_id = user_id

    def save_client(self):
        """adding a client"""
        try:
            self.set_client("save")
            self.client_dao.add(self.client)
            print("The client has been added.")
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except ClientAlreadyExistsException as error:
            print(error.get_message())
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except DBConnectionException as error:
            print(error.get_message())
            if self.log:
                self.log.log_info(
                    'Main', 'save_client', 'Shutting down the system')
                self.log.log_debug(
                    'Main', 'save_client', 'Shutting down the system')

        except DBException as error:
            print(error.get_message())

    def update_client(self):
        """updating a client"""
        try:
            self.set_client("update")
            self.client_dao.modify(self.client)
            print("The client has been modified.")
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except ClientNotFoundException as error:
            print(error.get_message())
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except DBConnectionException as error:
            print(error.get_message())
            if self.log:
                self.log.log_info(
                    'Main', 'save_client', 'Shutting down the system')
                self.log.log_debug(
                    'Main', 'save_client', 'Shutting down the system')

        except DBException as error:
            print(error.get_message())

    def delete_client(self):
        """removing a client"""
        try:
            self.set_client("delete")
            self.client_dao.delete(self.client)
            print("The client has been deleted.")
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except ClientNotFoundException as error:
            print(error.get_message())
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except DBConnectionException as error:
            print(error.get_message())
            if self.log:
                self.log.log_info(
                    'Main', 'save_client', 'Shutting down the system')
                self.log.log_debug(
                    'Main', 'save_client', 'Shutting down the system')

        except DBException as error:
            print(error.get_message())

    def get_all_client(self):
        """"retrieving all clients"""
        try:
            clients = self.client_dao.get_clients()
            if clients:
                for client in clients:
                    print('%d %s %s' % (
                        client.user_id, client.host_name, client.user_name))

            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except DBConnectionException as error:
            print(error.get_message())
            if self.log:
                self.log.log_info(
                    'Main', 'save_client', 'Shutting down the system')
                self.log.log_debug(
                    'Main', 'save_client', 'Shutting down the system')

        except DBException as error:
            print(error.get_message())

    def set_node(self, type_of_operation):
        """Seeking for input from user"""
        if type_of_operation in ("save", "update"):
            node_id = input("Enter id : ")
            user_name = input("Enter name: ")
            host_name = input("Enter hostname : ")
            port = input("Enter portname : ")
            status = input("Enter status: ")
            self.node.name = user_name
            self.node.node_id = node_id
            self.node.host_name = host_name
            self.node.port = port
            self.node.status = status

        elif type_of_operation == "delete":
            node_id = input("Enter id : ")
            self.node.node_id = node_id

    def save_node(self):
        """adding a new node into system"""
        try:
            self.set_node("save")
            self.node_dao.add(self.node)
            print("The node has been added.")
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except NodeAlreadyExistsException as error:
            print(error.get_message())
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except DBConnectionException as error:
            print(error.get_message())
            if self.log:
                self.log.log_info(
                    'Main', 'save_client', 'Shutting down the system')
                self.log.log_debug(
                    'Main', 'save_client', 'Shutting down the system')

        except DBException as error:
            print(error.get_message())

    def update_node(self):
        """updating a node"""
        try:
            self.set_node("update")
            self.node_dao.modify(self.node)
            print("The node has been updated.")
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except NodeNotFoundException as error:
            print(error.get_message())
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except DBConnectionException as error:
            print(error.get_message())
            if self.log:
                self.log.log_info(
                    'Main', 'save_client', 'Shutting down the system')
                self.log.log_debug(
                    'Main', 'save_client', 'Shutting down the system')

        except DBException as error:
            print(error.get_message())

    def delete_node(self):
        """removing a node"""
        try:
            self.set_node("delete")
            self.node_dao.delete(self.node)
            print("The node has been deleted.")
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except NodeNotFoundException as error:
            print(error.get_message())
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except DBConnectionException as error:
            print(error.get_message())
            if self.log:
                self.log.log_info(
                    'Main', 'save_client', 'Shutting down the system')
                self.log.log_debug(
                    'Main', 'save_client', 'Shutting down the system')

        except DBException as error:
            print(error.get_message())

    def get_all_available_nodes(self):
        """retrieving all available nodes"""
        try:
            nodes = self.node_dao.get_available_nodes()
            if nodes:
                for node in nodes:
                    print('%d %s %s %d %d' % (
                        node.node_id, node.name, node.host_name, node.port, node.status))

            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except DBConnectionException as error:
            print(error.get_message())
            if self.log:
                self.log.log_info(
                    'Main', 'save_client', 'Shutting down the system')
                self.log.log_debug(
                    'Main', 'save_client', 'Shutting down the system')

        except DBException as error:
            print(error.get_message())

    def get_all_nodes(self):
        """retrieving all nodes"""
        try:
            nodes = self.node_dao.get_all_nodes()
            if nodes:
                for node in nodes:
                    print('%d %s %s %s %s' % (
                        node.node_id, node.name, node.host_name, node.port, node.status))

            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except DBConnectionException as error:
            print(error.get_message())
            if self.log:
                self.log.log_info(
                    'Main', 'save_client', 'Shutting down the system')
                self.log.log_debug(
                    'Main', 'save_client', 'Shutting down the system')

        except DBException as error:
            print(error.get_message())

    def set_task(self, type_of_operation):
        """Seeking for input from user"""
        if type_of_operation in ("save", "update"):
            task_id = input("Enter Task id : ")
            task_name = input("Enter Task name: ")
            task_exe_path = input("Enter Task Execution Path : ")
            self.task_instance.task_name = task_name
            self.task_instance.task_id = task_id
            self.task_instance.task_exe_path = task_exe_path

        elif type_of_operation == "delete":
            task_id = input("Enter task id : ")
            self.task_instance.task_id = task_id

    def save_task(self):
        """adding a new task in task queue"""
        try:
            self.set_task("save")
            self.task_dao.add(self.task_instance)
            print("The new task has been added.")
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except TaskAlreadyExistsException as error:
            print(error.get_message())
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except DBConnectionException as error:
            print(error.get_message())
            if self.log:
                self.log.log_info(
                    'Main', 'save_client', 'Shutting down the system')
                self.log.log_debug(
                    'Main', 'save_client', 'Shutting down the system')

        except DBException as error:
            print(error.get_message())

    def update_task(self):
        """updating a task in task queue"""
        try:
            self.set_task("update")
            self.task_instance.task_state = 'None'
            self.task_instance.task_status = 'None'
            self.task_instance.task_error_message = 'None'
            self.task_instance.task_result = 'None'
            self.task_instance.task_parameters = 'None'
            self.task_instance.client_id = 1
            self.task_instance.node_id = 1
            self.task_dao.modify(self.task_instance)
            print("The task has been updated")
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except TaskAlreadyExistsException as error:
            print(error.get_message())
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except TaskNotFoundException as error:
            print(error.get_message())
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except DBConnectionException as error:
            print(error.get_message())
            if self.log:
                self.log.log_info(
                    'Main', 'save_client', 'Shutting down the system')
                self.log.log_debug(
                    'Main', 'save_client', 'Shutting down the system')

        except DBException as error:
            print(error.get_message())

    def delete_task(self):
        try:
            self.set_task("delete")
            self.task_dao.delete(self.task_instance)
            print("The task has been deleted.")
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except TaskNotFoundException as error:
            print(error.get_message())
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except DBConnectionException as error:
            print(error.get_message())
            if self.log:
                self.log.log_info(
                    'Main', 'save_client', 'Shutting down the system')
                self.log.log_debug(
                    'Main', 'save_client', 'Shutting down the system')

        except DBException as error:
            print(error.get_message())

    def get_all_tasks_by_id(self):
        """retrieving tasks by its task id"""
        try:
            task_id = int(input('Enter task id : '))
            task = self.task_dao.get_task_by_id(task_id)
            print('%d %s %s' % (
                task.task_id, task.task_name, task.task_exe_path))

            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except TaskNotFoundException as error:
            print(error.get_message())
            print("\n")
            print("Choose Operations to Perform : ")
            input_for_initial = self.get_input('initial')
            if input_for_initial is not 4:
                input_for_next = self.get_input('next')
                self.call_operations(input_for_initial, input_for_next)
            else:
                if self.log:
                    self.log.log_info(
                        'Main', 'save_client', 'Shutting down the system')
                    self.log.log_debug(
                        'Main', 'save_client', 'Shutting down the system')
                print("Bye")

        except DBConnectionException as error:
            print(error.get_message())
            if self.log:
                self.log.log_info(
                    'Main', 'save_client', 'Shutting down the system')
                self.log.log_debug(
                    'Main', 'save_client', 'Shutting down the system')

        except DBException as error:
            print(error.get_message())

    def call_operations(self, input_for_initial, input_for_next):
        if input_for_initial is 1:
            if input_for_next is 1:
                main_object.save_client()
            elif input_for_next is 2:
                main_object.update_client()
            elif input_for_next is 3:
                main_object.delete_client()
            elif input_for_next is 4:
                main_object.get_all_client()

        if input_for_initial is 2:
            if input_for_next is 1:
                main_object.save_node()
            elif input_for_next is 2:
                main_object.update_node()
            elif input_for_next is 3:
                main_object.delete_node()
            elif input_for_next is 4:
                main_object.get_all_nodes()

        if input_for_initial is 3:
            if input_for_next is 1:
                main_object.save_task()
            elif input_for_next is 2:
                main_object.update_task()
            elif input_for_next is 3:
                main_object.delete_task()
            elif input_for_next is 4:
                main_object.get_all_tasks_by_id()


main_object = Main()
input_for_initial = main_object.get_input('initial')
if input_for_initial is not 4:
    input_for_next = main_object.get_input('next')
    main_object.call_operations(input_for_initial, input_for_next)
else:
    log = LogManager.get_logger()
    if log:
        log.log_info(
            'Main', 'main', 'Shutting down the system')
        log.log_debug(
            'Main', 'main', 'Shutting down the system')
    print("Bye")
