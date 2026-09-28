"""This module defines the abstract transaction class for the banking system.
This class is meant to represent one transaction of currency on one persons account"""

from abc import ABC, abstractmethod
from decimal import Decimal
from transaction.transaction_status import TransactionStatus
from account.bank_account import BankAccount

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

class Transaction(ABC):
    """This class represents one transaction made by an account in the banking
      system.
    """

    def __init__(self,
                 transaction_id: str,
                 amount: Decimal,
                 status: TransactionStatus,
                 account: BankAccount) -> None:
        """Initializes a new instance of the BankAccount class.
        
            Args:
                transaction_id (str): The identification string for this transaction.
                amount (Decimal): The amount of money transferred in during this
                    transaction.
                status (TransactionStatus): The current status of this transaction
                account (BankAccount): The bank account from which this transaction
                    was made/recieved to
            
            Raises:
                ValueError: raised when
                    - transaction_id is blank string
                    - amount is less than or equal to zero

        """

        transaction_id = transaction_id.strip()
        if len(transaction_id) == 0:
            raise ValueError("transaction_id cannot be blank")

        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        

        self.__transaction_id = transaction_id
        self.__amount = amount
        self.__status = status
        self.__account = account

    @property
    def transaction_id(self) -> str:
        """Gets the transaction id of the transaction
        
            Returns:
                transaction_id (str): the transaction id
        """

        return self.__transaction_id

    @property
    def amount(self) -> Decimal:
        """Gets the amount of the transaction
        
            Returns:
                amount (Decimal): the transaction amount
        """

        return self.__amount

    @property
    def account(self) -> BankAccount:
        """Gets the BankAccount object of the account involved in the transaction
        
            Returns:
                account (BankAccount): the bank account involved in the transaction
        """

        return self.__account

    @property
    def status(self) -> TransactionStatus:
        """Gets the current status of the transaction
        
            Returns:
                status (TransactionStatus): the current status of the transaction
        """

        return self.__status

    @status.setter
    def status(self, status: TransactionStatus) -> None:
        """Updates the current transaction status
        
            Args:
                status (TransactionStatus): The new state to update the
                    transaction status to.
        """

        self.__status = status

    @abstractmethod
    @property
    def fees(self) -> Decimal:
        """Gets the fees associated with the transaction
        
            Returns:
                fees (Decimal): The fee amount
        """
        pass

    @abstractmethod
    def process(self) -> None:
        """Processes this transaction"""
        pass

    def __str__(self) -> str:
        """Returns the string representation of this Transaction Object
        
            Returns:
                str: The string representation of this transaction object
        """

        return (f"ID: {self.__transaction_id}"
                f"STATUS: {self.__status}"
                f"AMOUNT: {self.__amount}"
                f"SOURCE ACCT: {self.__account.account_id}")
    
