"""This module defines the concrete BasePercentageFeeStrategy interface"""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from decimal import Decimal
from fee.fee_strategy import FeeStrategy

class BasePercentageFeeStrategy(FeeStrategy):
    """This class is a concrete FeeStrategy subclass which calculates fees from
    the greater of a flat rate or a percentage of the transaction amount
    """

    def __init__(self, base_fee : Decimal, percentage : Decimal) -> None:
        """Initializes an instance of the BasePercentageFeeStrategy interface
        
            Args:
                base_fee (Decimal): The flat rate to charge as a minimum fee
                    if the percentage of the transaction amount is lower than
                    this base_fee
                percentage (Decimal): The percentage of the transaction amount
                    to charge as a fee amount, represented as a numebr between
                    0 and 1
            Raises:
                ValueError: raised when
                    - percentage is a value outside of the range 0-1 inclusive
                    - base_fee is a negative number
        """
        super().__init__()

        if base_fee < 0:
            raise(ValueError("base_fee must be greater than or equal to zero"))

        if percentage > 1 or percentage < 0:
            raise(ValueError("percentage must be a value between 0 and 1 (inclusive)"))

        self.__base_fee = base_fee
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

        return max(self.__base_fee, transaction_amount * self.__percentage)
        