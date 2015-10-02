"""LogManager to provide object of Logger Class"""

try:
    import threading
    from com.itt.tds.logs.Logger import Logger
    from com.itt.tds.db.exceptions.ConfigurationNotFoundException import ConfigurationNotFoundException
    from com.itt.tds.db.exceptions.ConfigurationLoadException import ConfigurationLoadException

except ImportError as error:
    print(error.__str__())


class LogManager(object):

    """LogManager to provide object of Logger Class"""
    __logger_instance = None
    __config_error = False

    def __init__(self):
        pass

    @staticmethod
    def get_logger():
        """Return the object of Logger class"""
        lock = threading.Lock()
        lock.acquire()

        try:
            if LogManager.__logger_instance is None and not LogManager.__config_error:
                try:
                    LogManager.__logger_instance = Logger()

                except ConfigurationNotFoundException as error:
                    LogManager.__config_error = True
                    raise ConfigurationNotFoundException(error.get_message())

                except ConfigurationLoadException as error:
                    LogManager.__config_error = True
                    raise ConfigurationLoadException(error.get_message())

        except ConfigurationNotFoundException as error:
            raise ConfigurationNotFoundException(error.get_message())

        except ConfigurationLoadException as error:
            raise ConfigurationLoadException(error.get_message())

        finally:
            lock.release()

        return LogManager.__logger_instance
