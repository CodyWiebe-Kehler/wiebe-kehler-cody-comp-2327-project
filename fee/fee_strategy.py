"""This module defines the abstract Fee_Strategy interface"""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from abc import ABC,abstractmethod
from decimal import Decimal

class FeeStrategy(ABC):
    """This class is the parent strategy interface for calculating
    fees for types of transactions
    """

    @abstractmethod
    def get_fee(self, transaction_amount : Decimal) -> Decimal:
        """This method calculates the fee amount on a certain transaction
        amount.
        
            Args:
                transaction_amount(Decimal): The amount of transferred in the
                    transaction
            Returns:
                fees (Decimal): The amount of fees to be paid for this transaction
        """
        pass