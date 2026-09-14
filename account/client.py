"""This module defines the client class for the banking system. This class is
meant to represent one client and their information."""

from email_validator import validate_email,EmailNotValidError
from account.account_status import AccountStatus

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

class Client():
    def __init__(self, client_id : int, name : str, email_address : str):

        if client_id <= 0:
            raise ValueError("client_id must be a value greater than zero")

        if len(name.strip()) == 0:
            raise ValueError("name cannot be an empty string")
        
        self.__client_id = client_id
        self.__name = name
        self.email_address = email_address

    @property
    def client_id(self) -> int:
        """Gets the client id of the client

        Returns:
            int: numeric client id for this client
        """

        return self.__client_id

    @property
    def name(self) -> str:
        """Gets the name of the client
        
        Returns:
            str: the name of the client
        """

        return self.__name

    @property
    def email_address(self) -> str:
        """Gets the clients email address
        
        Returns:
            str: the email address on file for the client
        """

        return self.__email_address

    @email_address.setter
    def email_address(self, email_address : str) -> None:
        """sets the value for the email address property"""

        try:
            # check_deliverability is set to false to not do network checks 
            # like seeing if the email address is actually registered or not
            valid_email = validate_email(email_address, check_deliverability = False)
            self.__email_address = valid_email

        except EmailNotValidError as exception:
            print(f"Error: {exception}")

    def __str__(self):
        return (f"{self.name} [{self.client_id}] - {self.email_address}")
        
    


