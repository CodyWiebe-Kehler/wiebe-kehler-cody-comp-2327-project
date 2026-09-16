import unittest

from email_validator import validate_email,EmailNotValidError
from account.client import Client

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method"""
    def test_client_id_less_than_0(self):
        #arrange
        client_id = -1 #test value
        name = "test client"
        email_address = "testemail@testdomain.com"

        #act
        with self.assertRaises(ValueError) as context:
            client = Client(client_id, name, email_address)

        #assert
        expected = "client_id must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected,actual)

    def test_client_id_is_0(self):
        #arrange
        client_id = 0 #test value
        name = "test client"
        email_address = "testemail@testdomain.com"

        #act
        with self.assertRaises(ValueError) as context:
            client = Client(client_id, name, email_address)

        #assert
        expected = "client_id must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected,actual)

    def test_name_empty_string(self):
        #arrange
        client_id = 1
        name = "" #test value
        email_address = "testemail@testdomain.com"

        #act
        with self.assertRaises(ValueError) as context:
            client = Client(client_id, name, email_address)

        #assert
        expected = "name cannot be an empty string"
        actual = str(context.exception)
        self.assertEqual(expected,actual)

    def test_email_invalid(self):
        #arrange
        client_id = 1
        name = "test client"
        email_address = "testemailtestdomain" #test value

        #act/assert
        with self.assertRaises(EmailNotValidError) as context:
            client = Client(client_id, name, email_address)

    def test_initialize_new_instance(self):
        #arrange
        client_id = 1
        name = "test client"
        email_address = "testemail@testdomain.com"

        #act 
        client = Client(client_id,name,email_address)

        #assert
        self.assertEqual(1, client._Client__client_id)
        self.assertEqual(name, client._Client__name)
        self.assertEqual(email_address, client._Client__email_address)

class TestClientIdProperty(unittest.TestCase):
    """Defines tests for the cleint id property"""

    def test_returns_current_state(self):
        #arrange
        client_id = 1
        name = "test client"
        email_address = "testemail@testdomain.com"
        client = Client(client_id,name,email_address)

        #act
        actual = client.client_id

        #assert
        expected = client_id
        self.assertEqual(actual,expected)

class TestNameProperty(unittest.TestCase):
    """Defines tests for the cleint name property"""

    def test_returns_current_state(self):
        #arrange
        client_id = 1
        name = "test client"
        email_address = "testemail@testdomain.com"
        client = Client(client_id,name,email_address)

        #act
        actual = client.name

        #assert
        expected = name
        self.assertEqual(actual,expected)

class TestClientIdProperty(unittest.TestCase):
    """Defines tests for the cleint email address property"""

    def test_returns_current_state(self):
        #arrange
        client_id = 1
        name = "test client"
        email_address = "testemail@testdomain.com"
        client = Client(client_id,name,email_address)

        #act
        actual = client.email_address

        #assert
        expected = email_address
        self.assertEqual(actual,expected)

    def test_set_to_invalid_email_address(self):
        #arrange
        client_id = 1
        name = "test client"
        email_address = "testemail@testdomain.com"
        client = Client(client_id, name, email_address)

        #act/assert
        with self.assertRaises(EmailNotValidError) as context:
            client.email_address = "testemailtestdomain.com"

    def test_set_email_address(self):
        #arrange
        client_id = 1
        name = "test client"
        email_address = "testemail@testdomain.com"
        client = Client(client_id,name,email_address)

        #act
        client.email_address = "testemail2@testdomain2.ca"

        #assert
        expected = "testemail2@testdomain2.ca"
        self.assertEqual(client.email_address,expected)

class TestStr(unittest.TestCase):
    """Defines tests for the __str__ method"""
    def test_returns_string_representation(self):
        #arrange
        client_id = 1
        name = "test client"
        email_address = "testemail@testdomain.com"
        client = Client(client_id,name,email_address)

        #act
        actual = str(client)

        #assert
        expected = "test client [1] - testemail@testdomain.com"
        self.assertEqual(actual,expected)

if __name__ == "__main__":
    unittest.main()