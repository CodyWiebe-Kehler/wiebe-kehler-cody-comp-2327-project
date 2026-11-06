import unittest

from fee import *
from decimal import Decimal

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method"""

    def test_percentage_greater_than_1(self):
        #arrange/act
        with self.assertRaises(ValueError) as context:
            fee_strategy = PercentageFeeStrategy(Decimal('1.10'))

        #Assert
        expected = "percentage must be a value between 0 and 1 (inclusive)"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_percentage_less_than_0(self):
        #arrange/act
        with self.assertRaises(ValueError) as context:
            fee_strategy = PercentageFeeStrategy(Decimal('-1.10'))

        #Assert
        expected = "percentage must be a value between 0 and 1 (inclusive)"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_initialize_new_instance(self):
        #arrage/act
        fee_strategy = PercentageFeeStrategy(Decimal('0.10'))

        #assert
        self.assertEqual(Decimal('0.10'), fee_strategy._PercentageFeeStrategy__percentage)

class TestGetFee(unittest.TestCase):
    """Defines tests for the get_fee method"""

    def test_get_fee(self):
        #arrage
        fee_strategy = PercentageFeeStrategy(Decimal('0.10'))

        #act
        fee = fee_strategy.get_fee(Decimal('100'))

        #assert
        expected = 10
        actual = fee
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()