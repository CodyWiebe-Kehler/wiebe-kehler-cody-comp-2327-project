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

        if account_id <= 0:
            raise ValueError("account_id must be a value greater than zero")
        
        self.__account_id = account_id
        self.__owner = owner
        self.__status = status
        self.balance = balance