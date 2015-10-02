
try:
    from com.itt.tds.comm.TDSController import TDSController
    from com.itt.tds.comm.TDSResponse import TDSResponse
    from com.itt.tds.db.dao_impl.DAOFactoryImpl import DAOFactoryImpl
    from com.itt.tds.model.ProcessingNode import ProcessingNode
    from com.itt.tds.db.exceptions.NodeAlreadyExistsException import NodeAlreadyExistsException
    from com.itt.tds.db.exceptions.DBException import DBException

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'ClientConnection', 'Import Module', error.__str__(), str(error))


class NodeController(TDSController):

    def process_request(self, request):
        """
            Description : process_request is a function which processes the request
            according to the request method and decides which will be the next
            method to work upon the request object.
        """
        if request.get_method() == "node-add":
            return self.add_node(request)

    def add_node(self, request):
        """
            Description : add_node function is responsible for adding node into
            the TDS Database. This function takes request object as an 
            aregument and extract the node information to store into database.
        """
        try:
            response = TDSResponse()
            node = ProcessingNode()
            node.name = request.headers['node-name']
            node.host_name = request.headers['node-ip']
            node.port = request.headers['node-port']
            node_dao = DAOFactoryImpl().get_dao('Node')
            response.set_status(node_dao.add(node))
            response.set_error_code(0)
            response.set_error_message('No Error')
            response.set_value('message', 'No Error')

        except NodeAlreadyExistsException as error:
            response.set_status('False')
            response.set_error_code(1)
            response.set_error_message(error.error_string)
            response.set_value('message', error.error_string)

        except DBException as error:
            response.set_status('False')
            response.set_error_code(1)
            response.set_error_message(error.error_string)
            response.set_value('message', error.error_string)

        response.set_protocol_type('response')
        response.set_protocol_format('JSON')
        response.set_protocol_version('1.0')

        return response
