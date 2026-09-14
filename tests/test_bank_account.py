import unittest

from account.account_status import AccountStatus
from account.client import Client
from account.bank_account import BankAccount

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method"""
    def test_account_id_less_than_0(self):
        #arrange
        account_id = -1 #test value
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE

        #act
        with self.assertRaises(ValueError) as context:
            account = BankAccount(account_id,balance,owner,status)

        #assert
        expected = "account_id must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected,actual)

    def test_account_id_is_0(self):
        #arrange
        account_id = 0 #test value
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE

        #act
        with self.assertRaises(ValueError) as context:
            account = BankAccount(account_id,balance,owner,status)

        #assert
        expected = "account_id must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected,actual)

    def test_initialize_new_instance(self):
        #arrange
        account_id = 1
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE

        #act
        account = BankAccount(account_id,balance,owner,status)

        #assert
        self.assertEqual(1,account._BankAccount__account_id)
        self.assertEqual(100,account._BankAccount__balance)
        self.assertEqual(owner,account._BankAccount__owner)
        self.assertEqual(AccountStatus.ACTIVE,account._BankAccount__status)

class TestAccountIdProperty(unittest.TestCase):
    def test_returns_current_state(self):
        #arrange
        account_id = 1
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE        
        account = BankAccount(account_id,balance,owner,status)

        #act
        actual = account.account_id

        #assert
        expected = account_id
        self.assertEqual(actual,expected)

class TestBalanceProperty(unittest.TestCase):
    def test_returns_current_state(self):
        #arrange
        account_id = 1
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE        
        account = BankAccount(account_id,balance,owner,status)

        #act
        actual = account.balance

        #assert
        expected = balance
        self.assertEqual(actual,expected)

class TestOwnerProperty(unittest.TestCase):
    def test_returns_current_state(self):
        #arrange
        account_id = 1
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE        
        account = BankAccount(account_id,balance,owner,status)

        #act
        actual = account.owner

        #assert
        expected = owner
        self.assertEqual(actual,expected)

class TestStatusProperty(unittest.TestCase):
    def test_returns_current_state(self):
        #arrange
        account_id = 1
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE        
        account = BankAccount(account_id,balance,owner,status)

        #act
        actual = account.status

        #assert
        expected = status
        self.assertEqual(actual,expected)

class TestUpdateBalanceMethod(unittest.TestCase):
    def test_increase_balance(self):
        #arrange
        account_id = 1
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE        
        account = BankAccount(account_id,balance,owner,status)

        #act
        account.update_balance(100)

        #assert
        actual = 200
        self.assertEqual(account.balance,actual)

    def test_decrease_balance(self):
        #arrange
        account_id = 1
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE        
        account = BankAccount(account_id,balance,owner,status)

        #act
        account.update_balance(-100)

        #assert
        actual = 0
        self.assertEqual(account.balance,actual)

class TestDepositMethod(unittest.TestCase):
    def test_amount_less_than_0(self):
        #arrange
        account_id = 1
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE        
        account = BankAccount(account_id,balance,owner,status)

        #act
        with self.assertRaises(ValueError) as context:
            account.deposit(-100)

        #assert
        expected = "amount must be a value greater than or equal to zero"
        actual = str(context.exception)
        self.assertEqual(expected,actual)

    def test_deposit(self):
        #arrange
        account_id = 1
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE        
        account = BankAccount(account_id,balance,owner,status)

        #act
        account.update_balance(100)

        #assert
        actual = 200
        self.assertEqual(account.balance,actual)

class TestWithdrawlMethod(unittest.TestCase):
    def test_amount_less_than_0(self):
        #arrange
        account_id = 1
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE        
        account = BankAccount(account_id,balance,owner,status)

        #act
        with self.assertRaises(ValueError) as context:
            account.withdraw(-100)

        #assert
        expected = "amount must be a value greater than or equal to zero"
        actual = str(context.exception)
        self.assertEqual(expected,actual)

    def test_amount_is_0(self):
            #arrange
            account_id = 1
            balance = 100
            owner = Client(1,"test client","testemail@testdomain.com")
            status = AccountStatus.ACTIVE        
            account = BankAccount(account_id,balance,owner,status)
    
            #act
            account.withdraw(0)
    
            #assert
            expected = 100
            actual = account.balance
            self.assertEqual(expected,actual)

    def test_amount_greater_than_balance(self):
            #arrange
            account_id = 1
            balance = 100
            owner = Client(1,"test client","testemail@testdomain.com")
            status = AccountStatus.ACTIVE        
            account = BankAccount(account_id,balance,owner,status)
    
            #act
            with self.assertRaises(ValueError) as context:
                account.withdraw(101)
    
            #assert
            expected = "amount cannot exceed the account balance"
            actual = str(context.exception)
            self.assertEqual(expected,actual)

    def test_withdrawl(self):
        #arrange
        account_id = 1
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE        
        account = BankAccount(account_id,balance,owner,status)

        #act
        account.withdraw(100)

        #assert
        expected = 0
        self.assertEqual(account.balance,expected)

class TestStr(unittest.TestCase):

    def test_returns_string_representation(self):
        #arrange
        account_id = 1
        balance = 100
        owner = Client(1,"test client","testemail@testdomain.com")
        status = AccountStatus.ACTIVE        
        account = BankAccount(account_id,balance,owner,status)

        #act
        actual = str(account)

        #assert
        expected = "Account Number: 1 Balance: $100"
        self.assertEqual(expected,actual)






if __name__ == "__main__":
    unittest.main()