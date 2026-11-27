"""Defines the ClientServicesWindow class."""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from account import *
from ui.base.main_window import MainWindow
from ui.client_transaction_dialog import ClientTransactionDialog
from ui.client_services_about_dialog import ClientServicesAboutDialog

from PySide6.QtWidgets import (QTableWidget,
                               QTableWidgetItem)

from decimal import Decimal

class ClientServicesWindow(MainWindow):
    """Represents the primary window for viewing Client and Bank Account data"""

    def __init__(self) -> None:
        """Initializes and instance of the ClientServicesWindow class"""
        super().__init__()

        #create empty list of clients
        self.__clients = self.__load_client_data()

        #set UI default states
        self.setWindowTitle("Yarrow-Mullein Bank :: Client Services")
        self.__set_default_ui_state()

        self._client_number_line_edit.textChanged.connect(self.__client_number_changed)
        self._search_button.clicked.connect(self.__search_button_clicked)
        
        self._exit_action.triggered.connect(self.__exit_action_clicked)
        self._clear_action.triggered.connect(self.__clear_action_clicked)
        self._about_action.triggered.connect(self.__about_action_clicked)
        self._account_table.itemDoubleClicked.connect(self.__account_double_clicked)

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
        
        clients = [["111","first name","last name","email@valid.com",
                 [["111111","111","10.1","1"],["2222222","111","20.22","1"]]]
                ]

        return clients

    def __set_default_ui_state(self) -> None:
        """Configures UI widgets to thier default expected states"""
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

    def __client_number_changed(self) -> None:
        """handles onclicked event for client number line edit text changed"""
        self.__set_default_ui_state()

    def __search_button_clicked(self) -> None:
        """Handles onclicked event for search button clicked"""
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

    def __exit_action_clicked(self) -> None:
        """Handles the on clicked event for exit action"""
        self.close()

    def __clear_action_clicked(self) -> None:
        """Handles the on clicked event for clear action"""
        self.__set_default_ui_state()
        self._client_number_line_edit.setText("")

    def __about_action_clicked(self) -> None:
        """Handles the on clicked event for about action"""
        about_dialog = ClientServicesAboutDialog()
        about_dialog.exec()

    def __find_selected_account(self, currentTableWidgetItem: QTableWidgetItem) -> list:
        """Helper function which returns a reference to the array in self.__clients 
            that is represented by the passed in QTableWidgetItem.
            
            Args:
                currentTableWidgetItem (QTableWidgetItem): The table widget item
                    you want to find the matching self.__clients account array for
                    
            Returns:
                list[str]: The reference to the self.__clients array representing
                    the account that matches the input tableWidget
        """
        #grab currently selected client from self.__clients based on searched client number
        curClient = []
        for client in self.__clients:
            if client[0] == self._client_number_line_edit.text():
                curClient = client

        #pull the account based on selected widget row
        accounts = client[4]
        accountArray = accounts[currentTableWidgetItem.row()]

        return accountArray


    def __account_double_clicked(self, selectedTableWidget: QTableWidgetItem) -> None:
        """Handles onclicked event for the account table by opening 
            ClientTransactionDialog for selected account
        
            args:
                item (QTableWidgetItem): The cell of the table that was double 
                    clicked on
        """

        #grabs client and account from self.__clients based off table selection
        # and client number line edit 
        curClient = []
        for client in self.__clients:
            if client[0] == self._client_number_line_edit.text():
                curClient = client
        
        accountArray = self.__find_selected_account(selectedTableWidget)

        #creates Client and BankAccount objects from the stored arrays 
        clientObj = Client(int(curClient[0]),f"{curClient[1]} {curClient[2]}",curClient[3])
        accountObj = BankAccount(int(accountArray[0]),Decimal(accountArray[2]), client, AccountStatus(int(accountArray[3])))
        print(f"Selected Client {clientObj}")
        print(f"Selected Account{accountObj}")

        #opens ClientTransactionDialog with the accountObj for reference
        TransactionDialog = ClientTransactionDialog(accountObj)
        TransactionDialog._process_transaction.connect(self.__process_transaction)
        TransactionDialog.exec()

    def __process_transaction(self,updatedAccount: BankAccount):
        """Handles an incoming transaction, and applies it to the appropriate account
        
            args:
                account (BankAccount): The bank account object, with the updated
                    balance from the transaction dialog
        """

        print(f"transaction signalled, new account: {updatedAccount}")
        #get selected account
        item = self._account_table.selectedItems()[0]
        accountArray = self.__find_selected_account(item)
        print(accountArray)

        #update self.__clients arrays to match passed in account balance value

        accountArray[2] = str(updatedAccount.balance)

        #refresh UI and table with current information
        self.__set_default_ui_state()
        self.__search_button_clicked()



