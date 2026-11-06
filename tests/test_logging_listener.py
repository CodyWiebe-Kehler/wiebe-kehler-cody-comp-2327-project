import unittest

from transaction import *
from events import *
from account import *
from decimal import Decimal

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

class TestUpdate(unittest.TestCase):
    """Defines tests for the update method"""

    def test_sender_type_not_transaction(self):
        #arrange
        listener = LoggingListener()
        sender = Decimal('1')
        #act
        with self.assertRaises(TypeError) as context:
            listener.update(sender)

        #assert
        expected = "sender must be a Transaction type"
        actual = str(context.exception)
        self.assertEqual(expected,actual)
