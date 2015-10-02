"""Client class"""


class Client:

    """Client class contains methods for store and retrieve client information"""

    def __init__(self):
        """initialization function for client object"""
        self._host_name = None
        self._user_name = None
        self._user_id = None

    @property
    def host_name(self):
        """getting client host name"""
        return self._host_name

    @host_name.setter
    def host_name(self, host_name_value):
        """setting client host name"""
        self._host_name = host_name_value

    @property
    def user_name(self):
        """getting client user name"""
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """setting client user name"""
        self._user_name = user_name

    @property
    def user_id(self):
        """getting client user id"""
        return self._user_id

    @user_id.setter
    def user_id(self, user_id_value):
        """setting client user id"""
        self._user_id = user_id_value
