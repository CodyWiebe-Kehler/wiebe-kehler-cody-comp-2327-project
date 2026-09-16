"""This module defines the client class for the banking system. This class is
meant to represent one client and their information."""

from account.account_status import AccountStatus
from account.client import Client
from decimal import Decimal

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

class BankAccount():
    def __init__(self, account_id : int, balance : Decimal, owner : Client, 
                 status: AccountStatus):

        """Initializes a new instance of the BankAccount class.

        Args:
            account_id (int): The identification number for this bank account
                instance.
            balance (Decimal): The current bank account balance at the time of
                instance creation.
            owner (Client): The Client object instance representing the owner 
                of this bank account.
            status (AccountStatus): The current state of the account, where
                the value is one of the AccountStatus enumeration values. 
        
        Raises:
            ValueError: Raised when the account_id parameter is passed in as
                a value that is less than zero.
        """

        if account_id <= 0:
            raise ValueError("account_id must be a value greater than zero")
        
        self.__account_id = account_id
        self.__owner = owner
        self.__status = status
        self.__balance = balance

    @property
    def account_id(self) -> int:
        """Gets the account id of the account
        
        Returns:
            int: numeric account id for this account
        """

        return self.__account_id

    @property
    def owner(self) -> Client:
        """Gets the Client object representing the owner of this account
        
        Returns:
            Client: client object representing the owner of this account
        """

        return self.__owner

    @property
    def status(self):
        """Gets the AccountStatus enumeration value representing the current status
        of this account
                
        Returns:
            AccountStatus: AccountStatus enumeration value representing the 
            status of this account
        """

        return self.__status


    @property
    def balance(self) -> Decimal:
        """Gets the balance of the account
        
        Returns:
            Decimal: decimal value of the balance of the account
        """

        return self.__balance

    def __str__(self):
        """Returns the string representation of the BankAccount instance
        
        Returns:
            str: The string representation of the BankAccount instance
        """

        return f"Account Number: {self.account_id} Balance: ${self.__balance}"

    def update_balance(self, amount : Decimal) -> None:
        """Changes the balance of the account by the amount argument. Can be 
        incremented or decremented with positive or negative values respectively.
                
        Arguments:
            Amount (Decimal): decimal value to adjust the account balance by.
        """

        self.__balance = self.__balance + amount

    def deposit(self, amount : Decimal) -> None:
        """Adds the given amount to the balance of the account, amount must be 
        positive
                    
            Arguments:
                Amount (Decimal): positive decimal value to add to the account balance.
        """

        if amount < 0:
            raise ValueError("amount must be a value greater than or equal to zero")

        self.__balance = self.__balance + amount

    def withdraw(self, amount : Decimal) -> None:
        """Subtracts the given amount from the balance of the account, amount must be 
        positive
                    
            Arguments:
                Amount (Decimal): positive decimal value to subtract from the account balance.
        """

        if amount < 0:
            raise ValueError("amount must be a value greater than or equal to zero")

        if amount > self.__balance:
            raise ValueError("amount cannot exceed the account balance")

        self.__balance = self.__balance - amount
