import unittest

from transaction.transaction_status import TransactionStatus

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

class TestTransactionStatus(unittest.TestCase):
    """Defines tests for the TransactionStatus Enumeration values initiation"""
    def test_enumeration_values_initialized(self):
        self.assertEqual(1, TransactionStatus.PENDING.value)
        self.assertEqual(2, TransactionStatus.PROCESSED.value)
        self.assertEqual(3, TransactionStatus.FAILED.value)

if __name__ == "__main__":
    unittest.main()