
import mysql.connector

from DBManager import DBManager


class DBManagerImpl(DBManager):

    def __init__(self, user_name='', password='', host_name='', db_name=''):
        self.hostName = host_name
        self.userName = user_name
        self.password = password
        self.dbName = db_name
        self.connectObject = None

    def get_connection(self):
        try:
            self.connectObject = mysql.connector.connect(
                user=self.userName, password=self.password, host=self.hostName, db=self.dbName)

        except mysql.connector.Error as e:
            print(e.__str__())
            exit()

    def close_connection(self):
        try:
            self.connectObject.close()
        except mysql.connector.Error as e:
            print(e.__str__())

    def execute_dml_query(self, query, type_of_operation):
        try:
            cur = self.connectObject.cursor()

            if type_of_operation == "Insert":
                cur.execute(query)
                self.connectObject.commit()
                return_value = cur.lastrowid
                return return_value

            elif type_of_operation == "Select":
                cur.execute(query)
                self.connectObject.commit()
                return_value = cur.rowcount
                return return_value

            elif type_of_operation == "Update":
                cur.execute(query)
                self.connectObject.commit()

            elif type_of_operation == "Delete":
                cur.execute(query)
                self.connectObject.commit()

        except mysql.connector.Error as e:
            print(e.__str__())

        except Exception:
            print("Cursor Attribute Error")

        finally:
            if cur is not None:
                cur.close()

    def execute_select_query(self, query):
        try:
            cur = self.connectObject.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            return rows

        except Exception:
            print("Cursor Attribute Error")

        finally:
            if cur is not None:
                cur.close()
