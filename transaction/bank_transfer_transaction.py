"""This module defines the BankTransferTransaction class deriving from the
parent Transaction class"""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from transaction.transaction import Transaction
from transaction.transaction_status import TransactionStatus
from account.bank_account import BankAccount
from account.account_status import AccountStatus
from decimal import Decimal

class BankTransferTransaction(Transaction):
    """This class represents a transaction where funds are transferred from a 
    source account to a target account
    """

    def __init__(self, 
                 transaction_id: str, 
                 amount: Decimal, 
                 status: TransactionStatus, 
                 account: BankAccount,
                 target_account : BankAccount) -> None:
        """Initializes an instance of the BankTransferTransaction class
        
            Args:
                transaction_id (str): The identification string for this transaction.
                amount (Decimal): The amount of money transferred in during this
                    transaction.
                status (TransactionStatus): The current status of this transaction
                account (BankAccount): The bank account from which the funds will
                    be transferred from
                target_account (BankAccount): The bank account the funds will
                    be transferred to
                        
            Raises:
                ValueError: raised when
                    - transaction_id is blank string
                    - amount is less than or equal to zero"""
        
        super().__init__(transaction_id, amount, status, account)

        self.__target_account = target_account

    @property
    def fees(self) -> Decimal:
        """Returns the fees to debit from the account when the transaction
        is processed. Amount is the greater of $1.00 or 0.7% of the transaction
        amount.
            
            Returns:
                fees (Decimal): The amount of money to debit from the account
                    as part of transaction fees"""
        
        return max(Decimal(1.00), self.amount * 0.7)

    def process(self) -> None:
        """This method processes the transaction, transferring the money amount 
        from the this transaction objects source account to its target account.
        if the process cannot be completed transaction status will be set to 
        FAILED, otherwise it will be set to PROCESSED"""

        #validates all accounts are active and source account has enough money
        if ( (self.account.status != AccountStatus.ACTIVE) or 
            (self.__target_account.status != AccountStatus.ACTIVE) or
            ( (self.amount + self.fees) > self.account.balance) ):
            self.status = TransactionStatus.FAILED 

        elif self.status == TransactionStatus.PENDING:
            self.account.withdraw(self.amount)
            self.account.withdraw(self.fees)
            self.__target_account.deposit(self.amount)
            self.status = TransactionStatus.PROCESSED

    def __str__(self) -> str:
        """Returns the string representation of this BankTransferTransaction Object
                
            Returns:
                str: The string representation of this object
        """

        return (f"{super().__str__()} --> TARGET ACCT: {self.__target_account.account_id}")