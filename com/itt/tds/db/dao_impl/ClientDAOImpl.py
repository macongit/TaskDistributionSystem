"""Client DAO Implementation"""

try:
    import mysql.connector
    from com.itt.tds.db.dao.ClientDAO import ClientDAO
    from com.itt.tds.db.dao_impl.DBDriverFactoryImpl import DBDriverFactoryImpl
    from com.itt.tds.cfg.TDSConfiguration import TDSConfiguration
    from com.itt.tds.logs.LogManager import LogManager
    from com.itt.tds.model.Client import Client
    from com.itt.tds.db.exceptions.ClientAlreadyExistsException import ClientAlreadyExistsException
    from com.itt.tds.db.exceptions.ClientNotFoundException import ClientNotFoundException

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'ClientDAOImpl', 'Import Module', error.__str__(), str(error))


class ClientDAOImpl(ClientDAO):

    """Client DAO Implementation"""

    def __init__(self):
        """Initialization method for implementation."""
        self.db_manager = DBDriverFactoryImpl().get_db_driver(
            TDSConfiguration().db_type)
        self.log = LogManager.get_logger()

    def add(self, client):
        """returns the newly added row id"""
        try:
            query = "INSERT into Client (id,hostname,user) values ('" + \
                str(client.user_id) + "','" + client.host_name + \
                "','" + client.user_name + "')"
            if self.log:
                self.log.log_debug('ClientDAOImpl', 'add', query)
            new_client = self.db_manager.execute_dml_query(query, "Insert")
            if self.log:
                self.log.log_info(
                    'ClientDAOImpl', 'add', "A new client with client id " + str(new_client) + " has been added")
            return True

        except mysql.connector.IntegrityError as error:
            error_code = error.__str__().split(':')[0]
            if self.log:
                self.log.log_error(
                    'ClientDAOImpl', 'add', error.__str__(), 'ClientAlreadyExistsException')
            raise ClientAlreadyExistsException(
                'Duplicate entry of for ' + str(client.host_name) + '-' + str(client.user_name), error_code)

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'ClientDAOImpl', 'add', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        finally:
            self.db_manager.close_connection()

    def modify(self, client):
        """updating client"""
        try:
            query = "SELECT id from Client where id = '" + \
                str(client.user_id) + "'"
            if self.log:
                self.log.log_debug('ClientDAOImpl', 'modify', query)
            row_id = self.db_manager.execute_select_query(query)
            if not row_id:
                raise ClientNotFoundException(
                    'client with client id ' + str(client.user_id) + ' does not exists.')
            else:
                query = "Update Client set user='" + str(client.user_name) + "',hostname='" + str(
                    client.host_name) + "' where id='" + str(client.user_id) + "'"
                if self.log:
                    self.log.log_debug('ClientDAOImpl', 'modify', query)
                self.db_manager.execute_dml_query(query, "Update")
                if self.log:
                    self.log.log_info('ClientDAOImpl', 'modify', "A client with client id " + str(
                        client.user_id) + " has been updated.")
                return True

        except ClientNotFoundException as error:
            if self.log:
                self.log.log_error(
                    'ClientDAOImpl', 'modify', error.get_message(), 'ClientNotFoundException')
            raise ClientNotFoundException(error.get_message())

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'ClientDAOImpl', 'modify', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        finally:
            self.db_manager.close_connection()

    def delete(self, client):
        """removing the client object"""
        try:
            query = "SELECT id from Client where id = '" + \
                str(client.user_id) + "'"
            if self.log:
                self.log.log_debug('ClientDAOImpl', 'modify', query)
            row_id = self.db_manager.execute_select_query(query)
            if not row_id:
                raise ClientNotFoundException(
                    'client of client id ' + str(client.user_id) + ' does not exists.')
            else:
                query = "delete from Client where id='" + \
                    str(client.user_id) + "'"
                if self.log:
                    self.log.log_debug('ClientDAOImpl', 'delete', query)
                self.db_manager.execute_dml_query(query, "Delete")
                if self.log:
                    self.log.log_info(
                        'ClientDAOImpl', 'delete', "A client with " + str(client.user_id) + " has been deleted.")
                return True

        except ClientNotFoundException as error:
            if self.log:
                self.log.log_error(
                    'ClientDAOImpl', 'delete', error.get_message(), 'ClientNotFoundException')
            raise ClientNotFoundException(error.get_message())

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'ClientDAOImpl', 'delete', error.__str__(), str(error))
            raise DBException(error_string, error_code)

        finally:
            self.db_manager.close_connection()

    def get_clients(self):
        """list out all the clients"""
        try:
            query = "SELECT * from Client"
            if self.log:
                self.log.log_debug('ClientDAOImpl', 'get_clients', query)
            rows = self.db_manager.execute_select_query(query)
            list_of_clients = []
            if rows:
                for row in rows:
                    client = Client()
                    client.user_id = row[0]
                    client.host_name = row[1]
                    client.user_name = row[2]
                    list_of_clients.append(client)
            return list_of_clients

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'ClientDAOImpl', 'get_clients', error.__str__(), str(error))
            raise DBException(error_string, error_code)

    def get_client(self, client_id):
        try:
            query = "SELECT * from Client where id = '" + str(client_id) + "'"
            if self.log:
                self.log.log_debug('ClientDAOImpl', 'get_client', query)
            rows = self.db_manager.execute_select_query(query)
            for row in rows:
                client = Client()
                client.user_id = row[0]
                client.host_name = row[1]
                client.user_name = row[2]
                return client
            return False

        except mysql.connector.DatabaseError as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'ClientDAOImpl', 'get_clients', error.__str__(), str(error))
            raise DBException(error_string, error_code)
