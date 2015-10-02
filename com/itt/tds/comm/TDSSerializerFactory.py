
from com.itt.tds.comm.TDSSerializer import TDSSerializer


class TDSSerializerFactory:

    @staticmethod
    def get_serializer():
        return TDSSerializer()
