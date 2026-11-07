"""This module defines the concrete PercentageFeeStrategy interface"""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from decimal import Decimal
from fee.fee_strategy import FeeStrategy

class PercentageFeeStrategy(FeeStrategy):
    """This class is a concrete FeeStrategy subclass which calculates fees from
      a percentage of the transaction amount
    """

    def __init__(self, percentage : Decimal) -> None:
        """Initializes an instance of the PercentageFeeStrategy interface
        
            Args:
                percentage (Decimal): The percentage of the transaction amount
                    to charge as a fee amount, represented as a numebr between
                    0 and 1
            Raises:
                ValueError: raised when
                    - percentage is a value outside of the range 0-1 inclusive
        """
        super().__init__()

        if percentage > 1 or percentage < 0:
            raise(ValueError("percentage must be a value between 0 and 1 (inclusive)"))

        self.__percentage = percentage


    def get_fee(self, transaction_amount : Decimal) -> Decimal:
        """This method calculates the fee amount on a certain transaction
        amount.
        
            Args:
                transaction_amount(Decimal): The amount of transferred in the
                    transaction
            Returns:
                fees (Decimal): The amount of fees to be paid for this transaction
        """

        return transaction_amount * self.__percentage
        