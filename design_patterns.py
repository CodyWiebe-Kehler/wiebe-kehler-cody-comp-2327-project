"""This module includes a program to demonstrate your understanding of
the Design Patterns used in this project.
"""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from transaction import *
from account import *
from fee import *
from events import *

from decimal import Decimal

def main() -> None:
    """The program's main entry point."""

    # 1. Create a transaction instance.
    client = Client(1, "test client", "testemail@test.com")
    account = BankAccount(1, Decimal('100'),client,AccountStatus.ACTIVE)
    transaction = CreditCardTransaction("1",Decimal('10'), TransactionStatus.PENDING, account,"auth code 1")
    # 2. Print the transaction fee
    print(f"Transaction fees: {transaction.fees}")
    # 3. Create a new instance of a fee strategy, the transaction fee
    #    is determined by base or percentage, depending which is higher.
    #    The base fee is $1.26 and the percentage of the transaction 
    #    amount is .07%.
    transaction_strategy_base_fee = BasePercentageFeeStrategy(Decimal('1.26'),Decimal('0.0007'))
    # 4. Update the transaction instance such that it will use the fee
    #    strategy to calculate the fees.
    transaction.set_fee_strategy(transaction_strategy_base_fee)
    # 5. Print the transaction fees. Formatting is not required.
    print(f"Transaction fee with base strategy: {transaction.fees}")
    # 6. Update the transaction instance such that the fee strategy will
    #    determine the fee based only on percentage of the transaction
    #    amount. The fee is .35% of the transaction amount.
    transaction_strategy_percentage = PercentageFeeStrategy(Decimal('0.0035'))
    transaction.set_fee_strategy(transaction_strategy_percentage)
    # 7. Print the transaction fees. Formatting is not required.
    print(f"Transaction fee with percentage strategy: {transaction.fees}")
    # 8. Create a logging listener instance.
    listener = LoggingListener()
    # 9. Using the listener, subscribe to the event.
    transaction._processed_event.add_listener(listener)
    # 10. Invoke the method to raise the event.
    transaction.process()

if __name__ == "__main__":
    main()
