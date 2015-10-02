"""Logger Interface"""


class LoggerInterface:

    """Logger Interface"""

    def log_warn(self, class_name, method_name, message, exception=None):
        pass

    def log_error(self, class_name, method_name, message, exception=None):
        pass

    def log_info(self, class_name, method_name, message, exception=None):
        pass

    def log_debug(self, class_name, method_name, message, exception=None):
        pass
