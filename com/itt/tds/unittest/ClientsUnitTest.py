
try:
    import unittest
    from com.itt.tds.db.dao_impl.ClientDAOImpl import ClientDAOImpl
    from com.itt.tds.model.Client import Client
    from com.itt.tds.db.exceptions.ClientAlreadyExistsException import ClientAlreadyExistsException
    from com.itt.tds.db.exceptions.ClientNotFoundException import ClientNotFoundException
    from com.itt.tds.db.exceptions.DBException import DBException

except ImportError as error:
    print(error.__str__())
    from com.itt.tds.logs.LogManager import LogManager
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'ClientUnitTest', 'Import Module', error.__str__(), str(error))


class ClientsUnitTest(unittest.TestCase):
    _client_dao = ClientDAOImpl()

    def setUp(self):
        """Initialization method for test cases which will run for each test 
        case"""
        self.test_data = self.read_data('test_data/clients.txt')

    def read_data(self, file_name):
        """Function is responsible for reading the given file and return the file
        data as dictionary
            Passing Arguments:
            file_name : Represents a file name which needs to be read

            Return Value:
            dictionary : Returns a dictionary type of object which stores the file 
            data as per line basis
        """
        test_data_dict = {}
        i = 0
        file_handler = open(file_name)
        for data in file_handler.readlines():
            if i == 0:
                pass
            else:
                if data[len(data) - 1] == '\n':
                    data = data[:len(data) - 1]
                test_data_dict[i] = data
            i += 1
        file_handler.close()
        return test_data_dict

#    @unittest.skip("Add client step")
    def test_01_add_client(self):
        """
        Test case for adding new client into the database.It is useful for 
        testing the functionality of 
        ClientDAO's add method."""
        try:
            for k, v in self.test_data.items():
                client = Client()
                test_str = v.split(',')
                client.user_id = test_str[0]
                client.host_name = test_str[1]
                client.user_name = test_str[2]
                ClientsUnitTest._client_dao.add(client)
                self.assertTrue(
                    ClientsUnitTest._client_dao.get_client(client.user_id))

            for k, v in self.test_data.items():
                client = Client()
                test_str = v.split(',')
                client.user_id = test_str[0]
                self.assertTrue(ClientsUnitTest._client_dao.delete(client))

        except DBException as error:
            print(error.get_message())

#    @unittest.skip("Add client step")
    def test_02_add_client_exception(self):
        """
        Test case for adding new client into the database.It is useful for 
        testing the functionality of 
        ClientDAO's add method.It should throw an exception because of adding
        the same client twice."""
        count = 0
        try:
            while count < 2:
                for k, v in self.test_data.items():
                    client = Client()
                    test_str = v.split(',')
                    client.user_id = test_str[0]
                    client.host_name = test_str[1]
                    client.user_name = test_str[2]
                    ClientsUnitTest._client_dao.add(client)
                    self.assertTrue(
                        ClientsUnitTest._client_dao.get_client(client.user_id))
                count += 1

        except ClientAlreadyExistsException as error:
            print(error.get_message())
            for k, v in self.test_data.items():
                client = Client()
                test_str = v.split(',')
                client.user_id = test_str[0]
                self.assertTrue(ClientsUnitTest._client_dao.delete(client))

        except DBException as error:
            print(error.get_message())

#    @unittest.skip("get all client step")
    def test_03_get_all_client(self):
        """
        Test case for getting all clients into the system."""
        try:
            return_value = ClientsUnitTest._client_dao.get_clients()
            self.assertGreater(len(return_value), 1)

        except DBException as error:
            print(error.error_string())

#    @unittest.skip("update client step")
    def test_04_update_client(self):
        """
        Test case for updating client into the database.It is useful for 
        testing the functionality of 
        ClientDAO's modify method."""
        for k, v in self.test_data.items():
            client = Client()
            test_str = v.split(',')
            client.user_id = test_str[0]
            client.host_name = test_str[1]
            client.user_name = test_str[2]
            ClientsUnitTest._client_dao.add(client)
            self.assertTrue(
                ClientsUnitTest._client_dao.get_client(client.user_id))

        for k, v in self.test_data.items():
            client = Client()
            test_str = v.split(',')
            client.user_id = test_str[0]
            client.host_name = test_str[1]
            client.user_name = test_str[2]
            ClientsUnitTest._client_dao.modify(client)
            client = ClientsUnitTest._client_dao.get_client(client.user_id)
            self.assertEqual(client.user_id, int(test_str[0]))
            self.assertEqual(client.host_name, test_str[1])
            self.assertEqual(client.user_name, test_str[2])

        for k, v in self.test_data.items():
            client = Client()
            test_str = v.split(',')
            client.user_id = test_str[0]
            self.assertTrue(ClientsUnitTest._client_dao.delete(client))

        try:
            for k, v in self.test_data.items():
                client = Client()
                test_str = v.split(',')
                client.user_id = test_str[0]
                client.host_name = test_str[1]
                client.user_name = test_str[2]
                self.assertTrue(ClientsUnitTest._client_dao.modify(client))

        except ClientNotFoundException as error:
            print(error.get_message())

        except DBException as error:
            print(error.get_message())


#    @unittest.skip("delete client step")
    def test_05_delete_client(self):
        """
        Test case for deleting client from the database.It is useful 
        for testing the functionality of 
        ClientDAO's delete method."""
        try:
            for k, v in self.test_data.items():
                client = Client()
                test_str = v.split(',')
                client.user_id = test_str[0]
                client.host_name = test_str[1]
                client.user_name = test_str[2]
                ClientsUnitTest._client_dao.add(client)
                self.assertTrue(
                    ClientsUnitTest._client_dao.get_client(client.user_id))

            for k, v in self.test_data.items():
                client = Client()
                test_str = v.split(',')
                client.user_id = test_str[0]
                self.assertTrue(ClientsUnitTest._client_dao.delete(client))

            for k, v in self.test_data.items():
                client = Client()
                test_str = v.split(',')
                client.user_id = test_str[0]
                self.assertTrue(ClientsUnitTest._client_dao.delete(client))

        except ClientAlreadyExistsException as error:
            print(error.get_message())

        except ClientNotFoundException as error:
            print(error.get_message())

        except DBException as error:
            print(error.get_message())

    def tearDown(self):
        return None

if __name__ == '__main__':
    unittest.main()
