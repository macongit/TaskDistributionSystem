"""Implementing LoggerInterface to create logs"""

try:
    import threading
    from com.itt.tds.logs.LoggerInterface import LoggerInterface
    from com.itt.tds.db.exceptions.ConfigurationNotFoundException import ConfigurationNotFoundException
    from com.itt.tds.db.exceptions.ConfigurationLoadException import ConfigurationLoadException
    from datetime import datetime
    import os

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'Logger', 'Import Module', error.__str__(), str(error))


class Logger(LoggerInterface):

    """Implementing LoggerInterface to create logs"""

    def __init__(self):
        """Initializing Logger Object"""
        from com.itt.tds.cfg.TDSConfiguration import TDSConfiguration
        self.log_file_path = TDSConfiguration().get_log_file_path()
        self.log_level = TDSConfiguration().get_log_level()
        self.file_object = None
        if not self.log_file_path:
            raise ConfigurationNotFoundException(
                "Log file path is not defined.")

        if not self.log_level:
            raise ConfigurationLoadException(
                "Log level not defined.")

    def log_warn(self, class_name, method_name, message, exception=None):
        """Logging a warning message with exception"""
        self.write_log_file(
            'warn', class_name, method_name, message, exception)

    def log_error(self, class_name, method_name, message, exception=None):
        """Logging a error message with exception"""
        self.write_log_file(
            'error', class_name, method_name, message, exception)

    def log_info(self, class_name, method_name, message, exception=None):
        """Logging a info message with exception"""
        self.write_log_file(
            'info', class_name, method_name, message, exception)

    def log_debug(self, class_name, method_name, message, exception=None):
        """Logging a debug message with exception"""
        self.write_log_file(
            'debug', class_name, method_name, message, exception)

    def write_log_file(self, level_of_log, class_name, method_name, message, exception=None):
        """Writing into log file"""

        lock = threading.Lock()
        lock.acquire()
        try:
            self.file_object = open(self.log_file_path, 'a')
        except FileNotFoundError as error:
            print(error.__str__())
        except OSError as error:
            print(error.__str__())

        else:
            expected_log_entries = None
            if self.log_level == 'error':
                expected_log_entries = 'error'
            elif self.log_level == 'warn':
                expected_log_entries = ('warn', 'error')
            elif self.log_level == 'info':
                expected_log_entries = ('info', 'warn', 'error')
            else:
                expected_log_entries = ('debug', 'info', 'warn', 'error')

            if level_of_log in expected_log_entries:
                if exception is not None:
                    formatted_message = '[' + level_of_log + ']' + ' [' + datetime.now().strftime(
                        '%Y-%m-%d %H:%M:%S') + ']' + ' [' + class_name + ']' + ' [' + method_name + '] : ' + exception + \
                        ' : ' + message + '\n'
                else:
                    formatted_message = '[' + level_of_log + ']' + ' [' + datetime.now().strftime(
                        '%Y-%m-%d %H:%M:%S') + ']' + ' [' + class_name + ']' + ' [' + method_name + '] : ' + message + \
                        '\n'
                self.file_object.write(formatted_message)
        finally:
            lock.release()
