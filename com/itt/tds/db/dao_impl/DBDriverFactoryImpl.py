"""DB Driver Factory Implementation"""

try:
    from com.itt.tds.db.dao.DBDriverFactory import DBDriverFactory
    from com.itt.tds.db.dao_impl.MysqlDBManagerImpl import MysqlDBManagerImpl

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'DBDriverFactoryImpl', 'Import Module', error.__str__(), str(error))


class DBDriverFactoryImpl(DBDriverFactory, object):

    """Implements DriverFactory interface, this implementation will
    return DB version of the type requested."""

    __db_factory_instance = None

    def __new__(cls):
        """Overriding __new__ method to make a singleton DB Driver object"""
        if DBDriverFactoryImpl.__db_factory_instance is None:
            return object.__new__(cls)
        else:
            return DBDriverFactoryImpl.__db_factory_instance

    def __init__(self):
        """@ReturnType void"""
        if DBDriverFactoryImpl.__db_factory_instance is None:
            DBDriverFactoryImpl.__db_factory_instance = self
            self.driver_object = None

    def get_db_driver(self, type_of_db):
        """@Return Driver Object of requested type"""
        if type_of_db == "Mysql":
            self.driver_object = DBDriverFactoryImpl.get_mysql_driver()
            return self.driver_object

    @staticmethod
    def get_mysql_driver():
        """return Mysql Driver object"""
        return MysqlDBManagerImpl()
