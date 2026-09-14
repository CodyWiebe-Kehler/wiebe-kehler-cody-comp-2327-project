import unittest

from account.account_status import AccountStatus

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

class TestAccountStatus(unittest.TestCase):
    def test_enumeration_values_initialized(self):
        self.assertEqual(0, AccountStatus.INACTIVE.value)
        self.assertEqual(1, AccountStatus.ACTIVE.value)
        self.assertEqual(2, AccountStatus.SUSPENDED.value)
        self.assertEqual(3, AccountStatus.CLOSED.value)

if __name__ == "__main__":
    unittest.main()