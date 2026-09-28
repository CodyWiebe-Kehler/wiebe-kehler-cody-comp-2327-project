import unittest

from account import *
from transaction import *
from decimal import Decimal

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method"""

    def setUp(self):
        self.valid_client = Client(1, "valid test client", "valid@email.com")
        self.valid_client_2 = Client(2, "valid client two", "valid2@email.com")
        self.valid_account = BankAccount(1, 100.50, self.valid_client, AccountStatus.ACTIVE)
        self.valid_account_2 = BankAccount(2, 200, self.valid_client_2, AccountStatus.ACTIVE)

    def test_transaction_id_blank(self):

        #arrange/act
        with self.assertRaises(ValueError) as context:
            transaction = BankTransferTransaction(" ", 50, TransactionStatus.PENDING,
                                     self.valid_account, self.valid_account_2)

        #Assert
        expected = "transaction_id cannot be blank"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_amount_less_than_zero(self):
    
        #arrange/act
        with self.assertRaises(ValueError) as context:
            transaction = BankTransferTransaction("test transaction", -50, TransactionStatus.PENDING,
                                        self.valid_account, self.valid_account_2)

        #Assert
        expected = "amount must be greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_amount_is_zero(self):
        
        #arrange/act
        with self.assertRaises(ValueError) as context:
            transaction = BankTransferTransaction("test transaction", 0, TransactionStatus.PENDING,
                                        self.valid_account, self.valid_account_2)

        #Assert
        expected = "amount must be greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_initilize_new_instance(self):

        #arrange/act
        transaction = BankTransferTransaction("test transaction", 1, TransactionStatus.PENDING,
                                                self.valid_account, self.valid_account_2)

        #assert
        self.assertEqual("test transaction", transaction._Transaction__transaction_id)
        self.assertEqual(1, transaction._Transaction__amount)
        self.assertEqual(TransactionStatus.PENDING, transaction._Transaction__status)
        self.assertEqual(self.valid_account, transaction._Transaction__account)
        self.assertEqual(self.valid_account_2, transaction._BankTransferTransaction__target_account)

class TestFeesProperty(unittest.TestCase):
    """Defines tests for the fees property"""

    def setUp(self):
        self.valid_client = Client(1, "valid test client", "valid@email.com")
        self.valid_client_2 = Client(2, "valid client two", "valid2@email.com")
        self.valid_account = BankAccount(1, 100.50, self.valid_client, AccountStatus.ACTIVE)
        self.valid_account_2 = BankAccount(2, 200, self.valid_client_2, AccountStatus.ACTIVE)

    def test_base_fee(self):

        #arrange/act
        transaction = BankTransferTransaction("test transaction", 1, TransactionStatus.PENDING,
                                            self.valid_account, self.valid_account_2)

        #assert
        self.assertEqual(1, transaction.fees)

    def test_percentage_fee(self):

        #arrange/act
        transaction = BankTransferTransaction("test transaction", 1000, TransactionStatus.PENDING,
                                                    self.valid_account, self.valid_account_2)

        #assert
        self.assertEqual(7, transaction.fees)

class TestProcessMethod(unittest.TestCase):
    """Defines tests for the process method"""

    def setUp(self):
        self.valid_client = Client(1, "valid test client", "valid@email.com")
        self.valid_client_2 = Client(2, "valid client two", "valid2@email.com")
        self.valid_account = BankAccount(1, 100.50, self.valid_client, AccountStatus.ACTIVE)
        self.valid_account_2 = BankAccount(2, 200, self.valid_client_2, AccountStatus.ACTIVE)
        self.inactive_account = BankAccount(3, 100, self.valid_client, AccountStatus.INACTIVE)
    
    def test_account_status_is_not_active(self):
        #arrange
        transaction = BankTransferTransaction("test transaction", 1, TransactionStatus.PENDING,
                                                            self.inactive_account, self.valid_account_2)

        #act
        transaction.process()

        #assert
        self.assertEqual(TransactionStatus.FAILED,transaction.status)

    def test_target_account_status_is_not_active(self):
        #arrange
        transaction = BankTransferTransaction("test transaction", 1, TransactionStatus.PENDING,
                                                            self.valid_account_2, self.inactive_account)

        #act
        transaction.process()
        
        #assert
        self.assertEqual(TransactionStatus.FAILED,transaction.status)

    def test_amount_and_fee_greater_than_balance(self):
        #arrange
        #transaction amount is JUST more than source account can afford including fees
        transaction = BankTransferTransaction("test transaction", 100, TransactionStatus.PENDING,
                                                            self.valid_account, self.valid_account_2)

        #act
        transaction.process()
        
        #assert
        self.assertEqual(TransactionStatus.FAILED,transaction.status)

    def test_transaction_processed(self):
        #arrange
        transaction = BankTransferTransaction("test transaction", 10, TransactionStatus.PENDING,
                                                            self.valid_account, self.valid_account_2)

        #act
        transaction.process()
        
        #assert
        self.assertEqual(TransactionStatus.PROCESSED,transaction.status)
        self.assertEqual(89.50,self.valid_account.balance)
        self.assertEqual(210, self.valid_account_2.balance)

class TestStr(unittest.TestCase):
    """Defines tests for the __str__ method"""

    def setUp(self):
        self.valid_client = Client(1, "valid test client", "valid@email.com")
        self.valid_client_2 = Client(2, "valid client two", "valid2@email.com")
        self.valid_account = BankAccount(1, 100.50, self.valid_client, AccountStatus.ACTIVE)
        self.valid_account_2 = BankAccount(2, 200, self.valid_client_2, AccountStatus.ACTIVE)
        self.inactive_account = BankAccount(3, 100, self.valid_client, AccountStatus.INACTIVE)

    def test_returns_string_representation(self):
        #act/arrange
        transaction = BankTransferTransaction("test transaction", 10, TransactionStatus.PENDING,
                                                                    self.valid_account, self.valid_account_2)

        #assert
        print(transaction)
        self.assertEqual(str(transaction), (f"ID: test transaction\n"
                                               f"STATUS: PENDING\n"
                                               f"AMOUNT: $10.00\n"
                                               f"SOURCE ACCT: 1 --> TARGET ACCT: 2"))
