"""Exception Class to handle the configuration load errors for TDS"""

try:
    from com.itt.tds.db.exceptions.ConfigurationException import ConfigurationException

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'ConfigurationLoadException', 'Import Module', error.__str__(), str(error))


class ConfigurationLoadException(ConfigurationException):

    """Exception Class to handle the configuration load errors for TDS"""

    def __init__(self, error_string):
        """initialization of ConfigurationLoadException exception object"""
        super().__init__(error_string)
        self.error_string = error_string
