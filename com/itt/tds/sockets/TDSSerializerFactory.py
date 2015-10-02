
from com.itt.tds.sockets.TDSSerializer import TDSSerializer


class TDSSerializerFactory:

    @staticmethod
    def get_serializer():
        return TDSSerializer()
