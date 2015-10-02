
try:
    import json
    from com.itt.tds.comm.TDSSerializerInterface import TDSSerializerInterface
    from com.itt.tds.comm.TDSRequest import TDSRequest
    from com.itt.tds.comm.TDSResponse import TDSResponse

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'TDSSerializer', 'Import Module', error.__str__(), str(error))


class TDSSerializer(TDSSerializerInterface):

    def deserialize(self, data):
        """
            Description : Function used to deserialize the data passed to it.

            Return Type : It returns a deserialize value of passed data.
        """
        json_data = json.loads(data.decode('utf-8'))

        if json_data['protocol_type'] == "request":
            request = TDSRequest()
            request.set_protocol_type(json_data['protocol_type'])
            request.set_source_ip(json_data['source_ip'])
            request.set_source_port(json_data['source_port'])
            request.set_destination_ip(json_data['dest_ip'])
            request.set_destination_port(json_data['dest_port'])
            request.set_header('node-name', json_data['headers']['node-name'])
            request.set_header('method', json_data['headers']['method'])
            request.set_header('node-port', json_data['headers']['node-port'])
            request.set_header('node-ip', json_data['headers']['node-ip'])
            request.set_header('message', json_data['headers']['message'])
            request.set_header(
                'protocol_version', json_data['headers']['protocol_version'])
            return request
        elif json_data['protocol_type'] == "response":
            response = TDSResponse()
            response.set_protocol_type(json_data['protocol_type'])
            response.set_source_ip(json_data['source_ip'])
            response.set_source_port(json_data['source_port'])
            response.set_destination_ip(json_data['dest_ip'])
            response.set_destination_port(json_data['dest_port'])
            response.set_header('status', json_data['headers']['status'])
            response.set_header(
                'error_message', json_data['headers']['error_message'])
            response.set_header('message', json_data['headers']['message'])
            response.set_header(
                'protocol_format', json_data['protocol_format'])
            return response

    def serialize(self, request):
        """
            Description : Function used to serialize the data passed to it.

            Return Type : It returns a serialize value of passed data.
        """
        return json.dumps(request.__dict__).encode('utf-8')
