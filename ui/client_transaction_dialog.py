"""Defines the ClientTransactionDialog class."""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from account import *

from ui.base.transaction_dialog import TransactionDialog

class ClientTransactionDialog(TransactionDialog):
    """Represents """

    def __init__(self, account: BankAccount) -> None:
        """Initializes an instance of a ClientTransactionDialog"""
        super().__init__()

        self.__account = account

        self.setWindowTitle("Yarrow-Mullein Bank :: Account Transaction")
        self.__set_default_ui_state()

    def __set_default_ui_state(self) -> None:
        """Configures the widgets to thier default state"""

        #sets values from account object
        self._account_number_label.setText(str(self.__account.account_id)) 
        self._current_balance_label.setText(f"${str(self.__account.balance)}")

        self._amount_line_edit.setText("")
        self._transaction_error_label.setText("")
        self._transaction_type_combobox.setCurrentIndex(-1)

        
        