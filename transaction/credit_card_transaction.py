"""This module defines the CreditCardTransaction class deriving from the
parent Transaction class"""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from transaction.transaction import Transaction
from transaction.transaction_status import TransactionStatus
from account.bank_account import BankAccount
from account.account_status import AccountStatus
from decimal import Decimal

class CreditCardTransaction(Transaction):
    """This class represents a transaction handled over credit card"""

    def __init__(self, 
                 transaction_id: str, 
                 amount: Decimal, 
                 status: TransactionStatus, 
                 account: BankAccount,
                 authorization_code: str) -> None:
        """Initializes an instance of the CreditCardTransaction class
                
            Args:
                transaction_id (str): The identification string for this transaction.
                amount (Decimal): The amount of money transferred in during this
                    transaction.
                status (TransactionStatus): The current status of this transaction
                account (BankAccount): The bank account from which the funds will
                    be transferred from
                target_account (BankAccount): The bank account the funds will
                    be transferred to
                authorization_code (str): The credit card transaction authorization
                    code
                        
            Raises:
                ValueError: raised when
                    - transaction_id is blank string
                    - amount is less than or equal to zero
        """
            
        super().__init__(transaction_id, amount, status, account)

        self.__authorization_code = authorization_code

    @property
    def fees(self) -> Decimal:
        """Returns the fees to debit from the account when the transaction
        is processed. Fees are 2% of transaction amount
            
            Returns:
                fees (Decimal): The amount of money to debit from the account
                    as part of transaction fees"""
        
        return self.amount * 0.02

    def process(self) -> None:
        """This method processes the transaction, withdrawing the amount and
        fees from the balance of the source account. if the process cannot be
        completed transaction status will be set to FAILED, otherwise it will
         be set to PROCESSED
        """

        #validates account is active, has enough money, and auth code isnt empty
        if ( (self.account.status != AccountStatus.ACTIVE) or 
            ( (self.amount + self.fees) > self.account.balance) or
            ( self.__authorization_code.strip() == "")):
            self.status = TransactionStatus.FAILED 

        elif self.status == TransactionStatus.PENDING:
            self.account.withdraw(self.amount)
            self.account.withdraw(self.fees)
            self.status = TransactionStatus.PROCESSED

    def __str__(self) -> str:
        """Returns the string representation of this CreditCardTransaction Object
                
            Returns:
                str: The string representation of this object
        """

        return (f"{super().__str__()}\n"
                f"AUTH CODE: {self.__authorization_code}")