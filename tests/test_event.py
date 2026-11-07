import unittest

from transaction import *
from events import *
from decimal import Decimal

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method"""

    def test_initialize_new_instance(self):
        #arrange/act
        event = Event()

        #assert
        expected = []
        actual = event._listeners
        self.assertEqual(expected,actual)

class TestAddListener(unittest.TestCase):
    """Defines tests for the add_listener method"""

    def test_add_listener_object(self):
        #arrange
        event = Event()

        #act
        test_listener = LoggingListener()
        event.add_listener(test_listener)

        #assert
        expected = [test_listener]
        actual = event._listeners
        self.assertEqual(expected,actual)

class TestRemoveListener(unittest.TestCase):
    """Defines tests for the remove_listener method"""

    def test_add_listener_object(self):
        #arrange
        event = Event()
        test_listener = LoggingListener()
        event.add_listener(test_listener)

        #act
        event.remove_listener(test_listener)

        #assert
        expected = []
        actual = event._listeners
        self.assertEqual(expected,actual)
