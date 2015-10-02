"""NodeDAO Implementation"""

try:
    import mysql.connector
    from com.itt.tds.db.dao.NodeDAO import NodeDAO
    from com.itt.tds.db.dao_impl.DBDriverFactoryImpl import DBDriverFactoryImpl
    from com.itt.tds.cfg.TDSConfiguration import TDSConfiguration
    from com.itt.tds.logs.LogManager import LogManager
    from com.itt.tds.model.ProcessingNode import ProcessingNode
    from com.itt.tds.NodeStates import NodeStates
    from com.itt.tds.db.exceptions.NodeAlreadyExistsException import NodeAlreadyExistsException
    from com.itt.tds.db.exceptions.NodeNotFoundException import NodeNotFoundException
    from com.itt.tds.db.exceptions.DBException import DBException

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'NodeDAOImpl', 'Import Module', error.__str__(), str(error))


class NodeDAOImpl(NodeDAO):

    """Node DAO Implementation"""

    def __init__(self):
        """"Initialization method for implementation."""
        self.db_manager = DBDriverFactoryImpl().get_db_driver(
            TDSConfiguration().db_type)
        self.log = LogManager.get_logger()

    def add(self, node):
        """return the newly added row id"""
        try:
            query = "INSERT into Node (name,hostname,port) values ('" + node.name + "','" + node.host_name + \
                    "','" + node.port + "')"
            if self.log:
                self.log.log_debug('NodeDAOImpl', 'add', query)
            new_node = self.db_manager.execute_dml_query(query, "Insert")
            if self.log:
                self.log.log_info(
                    'NodeDAOImpl', 'add', "A new node with node id " + str(new_node) + " has been added.")
            return True

        except mysql.connector.IntegrityError as error:
            error_code = error.__str__().split(':')[0]
            if self.log:
                self.log.log_error(
                    'NodeDAOImpl', 'add', error.__str__(), 'NodeAlreadyExistsException')
            raise NodeAlreadyExistsException(
                'Duplicate entry for ' + str(node.host_name) + ' - ' + str(node.name), error_code)

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'NodeDAOImpl', 'add', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        finally:
            self.db_manager.close_connection()

    def modify(self, node):
        """updating the node"""
        try:
            query = "SELECT id from Node where hostname = '" + \
                node.host_name + "' and name = '" + node.name + "'"
            if self.log:
                self.log.log_debug('NodeDAOImpl', 'modify', query)
            row_id = self.db_manager.execute_select_query(query)
            if not row_id:
                raise NodeNotFoundException(
                    'node with node hostname ' + str(node.host_name) + ' does not exists.')
            else:
                query = "Update Node set name='" + str(node.name) + "',hostname='" + str(node.host_name) + "',port='" + \
                        str(
                    node.port) + "',state='" + str(node.status) + "' where hostname = '" + node.host_name + "' and name = '" + node.name + "'"
                if self.log:
                    self.log.log_debug('NodeDAOImpl', 'modify', query)
                self.db_manager.execute_dml_query(query, "Update")
                if self.log:
                    self.log.log_info(
                        'NodeDAOImpl', 'modify', "A node with node hostname " + node.host_name + " has been updated")
                return True

        except NodeNotFoundException as error:
            if self.log:
                self.log.log_error(
                    'NodeDAOImpl', 'modify', error.get_message(), 'NodeNotFoundException')
            raise NodeNotFoundException(error.get_message())

        except mysql.connector.IntegrityError as error:
            error_code = error.__str__().split(':')[0]
            if self.log:
                self.log.log_error(
                    'NodeDAOImpl', 'add', error.__str__(), 'NodeAlreadyExistsException')
            raise NodeAlreadyExistsException(
                'Duplicate entry for ' + str(node.host_name) + '-' + str(node.name), error_code)

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'NodeDAOImpl', 'modify', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        finally:
            self.db_manager.close_connection()

    def delete(self, node):
        """deleting the node"""
        try:
            query = "SELECT id from Node where hostname = '" + \
                node.host_name + "' and name = '" + node.name + "'"
            if self.log:
                self.log.log_debug('NodeDAOImpl', 'delete', query)
            row_id = self.db_manager.execute_select_query(query)
            if not row_id:
                raise NodeNotFoundException(
                    'node with node hostname ' + node.host_name + ' does not exists.')
            else:
                query = "delete from Node where hostname='" + \
                    node.host_name + "' and name = '" + node.name + "'"
                if self.log:
                    self.log.log_debug('NodeDAOImpl', 'delete', query)
                self.db_manager.execute_dml_query(query, "Delete")
                if self.log:
                    self.log.log_debug(
                        'NodeDAOImpl', 'delete', "A node with node hostname " + node.host_name + " has been deleted")
                return True

        except NodeNotFoundException as error:
            if self.log:
                self.log.log_error(
                    'NodeDAOImpl', 'delete', error.get_message(), 'NodeNotFoundException')
            raise NodeNotFoundException(error.get_message())

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'NodeDAOImpl', 'delete', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        finally:
            self.db_manager.close_connection()

    def get_available_nodes(self):
        """ retrieving all the available nodes"""
        try:
            query = "SELECT * from Node where state = 1"
            if self.log:
                self.log.log_debug('NodeDAOImpl', 'get_available_nodes', query)
            rows = self.db_manager.execute_select_query(query)
            list_of_nodes = []
            if rows:
                for row in rows:
                    node = ProcessingNode()
                    node.node_id = row[0]
                    node.name = row[1]
                    node.host_name = row[2]
                    node.port = row[3]

                    if row[4] == NodeStates.IS_AVAILABLE:
                        node.status = 'available'
                    elif row[4] == NodeStates.IS_BUSY:
                        node.status = 'busy'
                    elif row[4] == NodeStates.IS_NONOPERATIONAL:
                        node.status = 'non-operational'

                    list_of_nodes.append(node)

            return list_of_nodes

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'NodeDAOImpl', 'get_all_available_nodes', error.__str__(), str(error))
            raise DBException(error_string, error_code)

    def get_node(self, host_name, name):
        try:
            query = "SELECT * from Node where hostname = '" + \
                host_name + "' and name = '" + name + "'"
            if self.log:
                self.log.log_debug('NodeDAOImpl', 'get_node', query)
            rows = self.db_manager.execute_select_query(query)
            if rows:
                for row in rows:
                    node = ProcessingNode()
                    node.node_id = row[0]
                    node.name = row[1]
                    node.host_name = row[2]
                    node.port = row[3]

                    if row[4] == NodeStates.IS_AVAILABLE:
                        node.status = 'available'
                    elif row[4] == NodeStates.IS_BUSY:
                        node.status = 'busy'
                    elif row[4] == NodeStates.IS_NONOPERATIONAL:
                        node.status = 'non-operational'

                return node
            else:
                return False

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'NodeDAOImpl', 'get_all_nodes', error.__str__(), str(error))
            raise DBException(error_string, error_code)

    def get_all_nodes(self):
        """list out all the nodes"""
        try:
            query = "SELECT * from Node"
            if self.log:
                self.log.log_debug('NodeDAOImpl', 'get_available_nodes', query)
            rows = self.db_manager.execute_select_query(query)
            list_of_nodes = []
            if rows:
                for row in rows:
                    node = ProcessingNode()
                    node.node_id = row[0]
                    node.name = row[1]
                    node.host_name = row[2]
                    node.port = row[3]

                    if row[4] == NodeStates.IS_AVAILABLE:
                        node.status = 'available'
                    elif row[4] == NodeStates.IS_BUSY:
                        node.status = 'busy'
                    elif row[4] == NodeStates.IS_NONOPERATIONAL:
                        node.status = 'non-operational'

                    list_of_nodes.append(node)

            return list_of_nodes

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'NodeDAOImpl', 'get_all_nodes', error.__str__(), str(error))
            raise DBException(error_string, error_code)
