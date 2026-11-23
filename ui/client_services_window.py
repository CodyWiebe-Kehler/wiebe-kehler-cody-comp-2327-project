"""Defines the ClientServicesWindow class."""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from account import *
from ui.base.main_window import MainWindow

class ClientServicesWindow(MainWindow):
    """Represents the primary window for viewing Client and Bank Account data"""

    def __init__(self):
        """Initializes and instance of the ClientServicesWindow class"""
        super().__init__()

        #create empty list of clients
        self.__clients = self.__load_client_data()

        #set UI default states
        self.setWindowTitle("Yarrow-Mullein Bank :: Client Services")
        self._search_button.setDefault(True)

        self._name_label.setText("")
        self._email_label.setText("")
        self._search_error_label.setHidden(True)

        #UI event handler connections
        #self._search_button.clicked.connect()

    def __load_client_data(self) -> list[Client]:
        """Returns a list of all clients and thier accounts in the system"""

        """returns fixed test data for our purposes
        
        test data format: ["client id", "first name", "last name", "email", list[account data]]
        where list[account data] = ["account id", "client id", "balance", "status"]
        
        where account status is a number in AccountStatus enumeration
        
        """
        
        return [["client id","first name","last name","email@valid.com",
                 ["account id","client id","balance","1"]]
                ]