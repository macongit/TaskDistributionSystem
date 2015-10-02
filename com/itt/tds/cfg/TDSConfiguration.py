"""TDS Configuration module which contains all the configuration
details regarding the application"""

try:
    import os
    import xml.dom.minidom
    from com.itt.tds.db.exceptions.ConfigurationNotFoundException import ConfigurationNotFoundException
    from com.itt.tds.logs.LogManager import LogManager

except ImportError as error:
    print(error.__str__())


class TDSConfiguration(object):

    """TDSConfiguration allows access to all the configuration specified
    in TDS.xml file.Example of the sample configuration file
    <tds>
    <database>
    <db-connection-string></db-connection-string>
    </database>
    </tds>"""
    __instance = None

    def __new__(cls):
        """Overriding the __new__ function to make
        a singleton object of TDSConfiguration"""
        if TDSConfiguration.__instance is None:
            return object.__new__(cls)
        else:
            return TDSConfiguration.__instance

    def __init__(self):
        """Constructor should be left private to ensure the object instance
        is created only once
        @ReturnType void##"""
        if TDSConfiguration.__instance is None:
            TDSConfiguration.__instance = self
            self.db_type = None
            self.db_details = {}

            try:
                try:
                    tds_dir_path = os.path.dirname(os.path.abspath(__file__))
                    file_object = xml.dom.minidom.parse(
                        tds_dir_path + r'\TDS.xml')

                except FileNotFoundError as error:
                    raise ConfigurationNotFoundException(error.__str__())

            except ConfigurationNotFoundException as error:
                if self.log:
                    self.log.log_error('TDSConfiguration', '__init__', error.get_message(
                    ), 'ConfigurationNotFoundException')
                raise ConfigurationNotFoundException(error.get_message())

            else:
                tds_root = file_object.documentElement
                database = tds_root.getElementsByTagName('database')
                database_string = database[0].getElementsByTagName('dbstring')
                self.db_type = database_string[0].getElementsByTagName(
                    'type')[0].childNodes[0].data
                self.db_details['username'] = database_string[
                    0].getElementsByTagName('username')[0].childNodes[0].data
                self.db_details['password'] = database_string[
                    0].getElementsByTagName('password')[0].childNodes[0].data
                self.db_details['hostname'] = database_string[
                    0].getElementsByTagName('hostname')[0].childNodes[0].data
                self.db_details['dbname'] = database_string[
                    0].getElementsByTagName('dbname')[0].childNodes[0].data

                logger = tds_root.getElementsByTagName('log')
                self.path_for_log_file = os.path.dirname(tds_dir_path) + '\\' + logger[0].getElementsByTagName(
                    'logfilepath')[0].childNodes[0].data
                self.log_level = logger[0].getElementsByTagName(
                    'loglevel')[0].childNodes[0].data
                self.log = LogManager.get_logger()
                if self.log:
                    self.log.log_info(
                        'TDSConfiguration', '__init__', "System is starting...")

                    self.log.log_info(
                        'TDSConfiguration', '__init__', "TDS.xml is reading up...")

                    self.log.log_info(
                        'TDSConfiguration', '__init__', "TDS logs has been prepared.")

    def get_db_type(self):
        """Returning Connecting DB type"""
        return self.db_type

    def get_db_connection_string(self):
        """@Returning DB Connection String"""
        return self.db_details

    def get_log_file_path(self):
        return self.path_for_log_file

    def get_log_level(self):
        return self.log_level
