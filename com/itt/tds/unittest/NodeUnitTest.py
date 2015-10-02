
try:
    import unittest
    from com.itt.tds.db.dao_impl.NodeDAOImpl import NodeDAOImpl
    from com.itt.tds.model.ProcessingNode import ProcessingNode
    from com.itt.tds.db.exceptions.NodeAlreadyExistsException import NodeAlreadyExistsException
    from com.itt.tds.db.exceptions.NodeNotFoundException import NodeNotFoundException

except ImportError as error:
    print(error.__str__())
    from com.itt.tds.logs.LogManager import LogManager
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'NodeUnitTest', 'Import Module', error.__str__(), str(error))


class NodeUnitTest(unittest.TestCase):
    _node_dao = NodeDAOImpl()

    def setUp(self):
        """Initialization method for test cases which will run for each test 
        case"""
        self.test_data = self.read_data('test_data/nodes.txt')

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

#    @unittest.skip("Add node step")
    def test_01_add_node(self):
        """
        Test case for adding new node into the database.It is useful for 
        testing the functionality of 
        NodeDAO's add method."""
        try:
            for k, v in self.test_data.items():
                node = ProcessingNode()
                test_str = v.split(',')
                node.node_id = test_str[0]
                node.name = test_str[1]
                node.host_name = test_str[2]
                node.port = test_str[3]
                node.status = test_str[4]
                NodeUnitTest._node_dao.add(node)
                self.assertTrue(
                    NodeUnitTest._node_dao.get_node(node.host_name, node.name))

            for k, v in self.test_data.items():
                node = ProcessingNode()
                test_str = v.split(',')
                node.name = test_str[1]
                node.host_name = test_str[2]
                self.assertTrue(NodeUnitTest._node_dao.delete(node))

        except NodeAlreadyExistsException as error:
            print(error.get_message())

#    @unittest.skip("Add node step")
    def test_02_add_node_exception(self):
        """
        Test case for adding new node into the database.It is useful for 
        testing the functionality of 
        NodeDAO's add method. It should throw an exception because of adding 
        the node twice."""
        try:
            count = 0
            while count < 2:
                for k, v in self.test_data.items():
                    node = ProcessingNode()
                    test_str = v.split(',')
                    node.node_id = test_str[0]
                    node.name = test_str[1]
                    node.host_name = test_str[2]
                    node.port = test_str[3]
                    node.status = test_str[4]
                    NodeUnitTest._node_dao.add(node)
                    self.assertTrue(
                        NodeUnitTest._node_dao.get_node(node.host_name, node.name))
                count += 1

        except NodeAlreadyExistsException as error:
            print(error.get_message())
            for k, v in self.test_data.items():
                node = ProcessingNode()
                test_str = v.split(',')
                node.name = test_str[1]
                node.host_name = test_str[2]
                self.assertTrue(NodeUnitTest._node_dao.delete(node))

#    @unittest.skip("get available node step")
    def test_03_get_available_nodes(self):
        """
        Test case for getting all available nodes in the system."""
        return_value = NodeUnitTest._node_dao.get_available_nodes()
        self.assertGreaterEqual(len(return_value), 1)

#    @unittest.skip("get all nodes step")
    def test_04_get_all_nodes(self):
        """
        Test case for getting all nodes in the system."""
        return_value = NodeUnitTest._node_dao.get_all_nodes()
        self.assertGreater(len(return_value), 1)

#    @unittest.skip("Update node step")
    def test_05_update_node(self):
        """
        Test case for updating node into the database.It is useful for 
        testing the functionality of 
        NodeDAO's modify method."""
        try:
            for k, v in self.test_data.items():
                node = ProcessingNode()
                test_str = v.split(',')
                node.node_id = test_str[0]
                node.name = test_str[1]
                node.host_name = test_str[2]
                node.port = test_str[3]
                node.status = test_str[4]
                NodeUnitTest._node_dao.add(node)
                self.assertTrue(
                    NodeUnitTest._node_dao.get_node(node.host_name, node.name))

            for k, v in self.test_data.items():
                node = ProcessingNode()
                test_str = v.split(',')
                node.node_id = test_str[0]
                node.name = test_str[1]
                node.host_name = test_str[2]
                node.port = test_str[3]
                node.status = test_str[4]
                NodeUnitTest._node_dao.modify(node)
                node = NodeUnitTest._node_dao.get_node(
                    node.host_name, node.name)
                self.assertEqual(node.name, test_str[1])
                self.assertEqual(node.host_name, test_str[2])
                self.assertEqual(node.port, test_str[3])

            for k, v in self.test_data.items():
                node = ProcessingNode()
                test_str = v.split(',')
                node.name = test_str[1]
                node.host_name = test_str[2]
                self.assertTrue(NodeUnitTest._node_dao.delete(node))

            for k, v in self.test_data.items():
                node = ProcessingNode()
                test_str = v.split(',')
                node.node_id = test_str[0]
                node.name = test_str[1]
                node.host_name = test_str[2]
                node.port = test_str[3]
                node.status = test_str[4]
                NodeUnitTest._node_dao.modify(node)
                node = NodeUnitTest._node_dao.get_node(
                    node.host_name, node.name)
                self.asserEqual(node.node_id, int(test_str[0]))
                self.asserEqual(node.name, test_str[1])
                self.asserEqual(node.host_name, test_str[2])
                self.asserEqual(node.port, int(test_str[3]))
                self.asserEqual(node.status, test_str[4])

        except NodeNotFoundException as error:
            print(error.get_message())

#    @unittest.skip("delete node step")
    def test_06_delete_node(self):
        """
        Test case for deleting node from the database.It is useful 
        for testing the functionality of 
        NodeDAO's delete method."""
        try:
            for k, v in self.test_data.items():
                node = ProcessingNode()
                test_str = v.split(',')
                node.node_id = test_str[0]
                node.name = test_str[1]
                node.host_name = test_str[2]
                node.port = test_str[3]
                node.status = test_str[4]
                NodeUnitTest._node_dao.add(node)
                self.assertTrue(
                    NodeUnitTest._node_dao.get_node(node.host_name, node.name))

            for k, v in self.test_data.items():
                node = ProcessingNode()
                test_str = v.split(',')
                node.name = test_str[1]
                node.host_name = test_str[2]
                self.assertTrue(NodeUnitTest._node_dao.delete(node))

            for k, v in self.test_data.items():
                node = ProcessingNode()
                test_str = v.split(',')
                node.name = test_str[1]
                node.host_name = test_str[2]
                self.assertTrue(NodeUnitTest._node_dao.delete(node))

        except NodeNotFoundException as error:
            print(error.get_message())

    def tearDown(self):
        return None

if __name__ == '__main__':
    unittest.main()
