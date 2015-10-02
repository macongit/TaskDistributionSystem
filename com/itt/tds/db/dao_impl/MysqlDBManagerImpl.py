"""MysqlDB Manager Implementation"""

try:
    import mysql.connector
    from com.itt.tds.db.dao.DBManager import DBManager
    from com.itt.tds.db.exceptions.DBConnectionException import DBConnectionException
    from com.itt.tds.cfg.TDSConfiguration import TDSConfiguration
    from com.itt.tds.db.exceptions.DBException import DBException
    from com.itt.tds.logs.LogManager import LogManager

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'MysqlDBManagerImpl', 'Import Module', error.__str__(), str(error))


class MysqlDBManagerImpl(DBManager):

    """MysqlDB Manager Implementation"""

    def __init__(self):
        """Initializing MysqlDB Manager Object """
        self.connection_object = None
        self.log = LogManager.get_logger()

    def get_connection(self, db_connection_string):
        """Getting Connection with mysql database"""
        try:
            self.connection_object = mysql.connector.connect(
                user=db_connection_string['username'],
                password=db_connection_string['password'],
                host=db_connection_string['hostname'],
                db=db_connection_string['dbname'])
            if self.log:
                self.log.log_info(
                    'MysqlDBManagerImpl', 'get_connection', 'Database Connection has been established')

        except mysql.connector.Error as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'MysqlDBManagerImpl', 'get_connection', error.__str__(), str(error))
            raise DBConnectionException(error_string, error_code)

    def close_connection(self):
        """Closing connection with mysql database"""
        try:
            self.connection_object.close()
            if self.log:
                self.log.log_info(
                    'MysqlDBManagerImpl', 'close_connection', 'Database Connection has been closed')

        except mysql.connector.Error as error:
            error_code = error.__str__().split(':')[0]
            error_string = error.__str__().split(':')[1]
            if self.log:
                self.log.log_error(
                    'MysqlDBManagerImpl', 'close_connection', error.__str__(), str(error))
            raise DBConnectionException(error_string, error_code)

    def execute_dml_query(self, query, type_of_query=None):
        """Executing DML Query"""
        self.get_connection(TDSConfiguration().get_db_connection_string())
        if self.connection_object is not None:
            cur = self.connection_object.cursor()
            return_value = ''
            cur.execute(query)
            self.connection_object.commit()
            if type_of_query == "Insert":
                return_value = cur.lastrowid
            if self.log:
                self.log.log_info('MysqlDBManagerImpl', 'execute_dml_query',
                                  'The number of rows affected are ' + str(cur.rowcount))
                self.log.log_debug('MysqlDBManagerImpl', 'execute_dml_query',
                                   'The number of rows affected are ' + str(cur.rowcount))

            cur.close()
            self.close_connection()
            return return_value

    def execute_select_query(self, query):
        """Executing Select Query"""
        self.get_connection(TDSConfiguration().get_db_connection_string())

        if self.connection_object is not None:
            cur = self.connection_object.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            if self.log:
                self.log.log_info('MysqlDBManagerImpl', 'execute_select_query',
                                  'The number of rows affected are ' + str(cur.rowcount))
                self.log.log_debug('MysqlDBManagerImpl', 'execute_select_query',
                                   'The number of rows affected are ' + str(cur.rowcount))

            cur.close()
            self.close_connection()
            return rows
