"""Defines the ClientServicesWindow class."""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from account import *
from ui.base.main_window import MainWindow

from PySide6.QtWidgets import (QTableWidget,
                               QTableWidgetItem)

class ClientServicesWindow(MainWindow):
    """Represents the primary window for viewing Client and Bank Account data"""

    def __init__(self):
        """Initializes and instance of the ClientServicesWindow class"""
        super().__init__()

        #create empty list of clients
        self.__clients = self.__load_client_data()

        #set UI default states
        self.setWindowTitle("Yarrow-Mullein Bank :: Client Services")
        self.__set_default_ui_state()

        self._client_number_line_edit.textChanged.connect(self.__client_number_changed)
        self._search_button.clicked.connect(self.__search_button_clicked)
        
        self._exit_action.triggered.connect(self.__exitActionClicked)
        self._clear_action.triggered.connect(self.__clearActionClicked)
        self._about_action.triggered.connect(self.__aboutActionClicked)

        #UI event handler connections
        #self._search_button.clicked.connect()

    def __load_client_data(self) -> list[Client]:
        """Returns a list of all clients and thier accounts in the system"""

        """returns fixed test data for our purposes
        
        test data format list[client]
        where client = ["client id", "first name", "last name", "email", list[account data]]
        where account data = ["account id", "client id", "balance", "status"]
        
        where account status is a number in AccountStatus enumeration
        
        """
        
        return [["client id","first name","last name","email@valid.com",
                 [["account id","client id","balance","1"],["account id 2","client id","balance 2","1"]]]
                ]

    def __set_default_ui_state(self):
        self._search_button.setEnabled(True)
        self._search_button.setDefault(True)
        self._client_number_line_edit.setFocus()

        #removes all rows and data from table, leaving table headers
        self._account_table.clearContents()
        while self._account_table.rowCount() > 0:
            self._account_table.removeRow(0)

        self._name_label.setText("")
        self._email_label.setText("")
        self._search_error_label.setHidden(True)

    def __client_number_changed(self):
        self.__set_default_ui_state()

    def __search_button_clicked(self):
        self._client_number_line_edit.setFocus()

        #temp storage for searched text and found client
        searchText = self._client_number_line_edit.text()
        found = False
        found_client = []
        #find client with that search text
        for client in self.__clients:
            if client[0] == searchText:
                found = True
                found_client = client

        if found:
            self._search_button.setEnabled(False)
            self._name_label.setText(f"{found_client[1]} {found_client[2]}")
            self._email_label.setText(found_client[3])

            for rowIndex,account in enumerate(found_client[4]):
                #add rows to table for each account in clients accounts
                accountNumWidget = QTableWidgetItem(account[0])
                accountBalanceWidget = QTableWidgetItem(account[2])
                #converts stored status int to string based on AccountStatus enumeration
                status = AccountStatus(int(account[3])).name
                accountStatusWidget = QTableWidgetItem(status)

                self._account_table.insertRow(rowIndex)
                self._account_table.setItem(rowIndex,0,accountNumWidget)
                self._account_table.setItem(rowIndex,1,accountBalanceWidget)
                self._account_table.setItem(rowIndex,2,accountStatusWidget)
                                                 
        else:
            #configure error display
            self._search_error_label.setEnabled(True)
            self._search_error_label.setHidden(False)
            self._search_error_label.setText("Client not found")

    def __exitActionClicked(self):
        self.close()

    def __clearActionClicked(self):
        self.__set_default_ui_state()
        self._client_number_line_edit.setText("")

    def __aboutActionClicked(self):
        pass