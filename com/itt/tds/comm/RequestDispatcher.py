try:
    from com.itt.tds.comm.NodeController import NodeController

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'RequestDispatcher', 'Import Module', error.__str__(), str(error))


class RequestDispatcher:

    @staticmethod
    def get_controller(request):
        """
            Description : get_controller is a static function which returns the 
            controller object based on request method.
        """
        if request.get_method() == "node-add":
            node_controller = NodeController()
            return node_controller
