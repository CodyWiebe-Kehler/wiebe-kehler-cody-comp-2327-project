"""Defines the ClientTransactionDialog class."""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from account import *

from ui.base.transaction_dialog import TransactionDialog

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal

class ClientTransactionDialog(TransactionDialog):
    """Represents a dialog window to make a transaction on the selected account"""

    _process_transaction = Signal(str)

    def __init__(self, account: BankAccount) -> None:
        """Initializes an instance of a ClientTransactionDialog"""
        super().__init__()

        self.__account = account

        self.setWindowTitle("Yarrow-Mullein Bank :: Account Transaction")
        self.__set_default_ui_state()

        #connect events and handlers
        self._process_transaction_button.clicked.connect(self.__process_button_clicked)

    def __set_default_ui_state(self) -> None:
        """Configures the widgets to thier default state"""

        #sets displayed values based on account object attribute
        self._account_number_label.setText(str(self.__account.account_id)) 
        self._current_balance_label.setText(f"${str(self.__account.balance)}")

        self._amount_line_edit.setText("")
        self._transaction_error_label.setText("")
        self._transaction_type_combobox.setCurrentIndex(-1)

    def __process_button_clicked(self):
        """Handles on clicked functionality for process button"""

        #transaction type not selected error
        if self._transaction_type_combobox.currentIndex == -1:
            self._transaction_error_label.setText("Please choose a transaction type")
            self._transaction_error_label.setHidden(False)
        #amount invalid error
        elif not self._amount_line_edit.text().isnumeric():
            self._transaction_error_label.setText("Please enter a valid amount")
            self._transaction_error_label.setHidden(False)
        #valid input
        else:
            self._transaction_error_label.setText("")
            self._transaction_error_label.setHidden(True)

            confirm = QMessageBox.question(self, "Process Transaction",
                                           f"{self._transaction_type_combobox.currentIndex} "
                                            f"${self._amount_line_edit.text()}"
                                            f"\nComplete this transaction?",
                                           QMessageBox.StandardButton.Yes | 
                                           QMessageBox.StandardButton.No | 
                                           QMessageBox.StandardButton.Cancel,
                                           QMessageBox.StandardButton.Cancel)

            if confirm == QMessageBox.StandardButton.Yes:
                try:
                    #process transaction
                    
                    self._process_transaction.emit("test")
                    self.done(0)
                except:
                    #error dialog
                    QMessageBox.critical(self,"Transaction Error",
                                         "An error occurred while processing the transaction",
                                         QMessageBox.StandardButton.Ok,
                                         QMessageBox.StandardButton.Ok)

                    self.done(1)

            elif confirm == QMessageBox.StandardButton.No:
                self.done(0)


        
        