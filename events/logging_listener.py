"""This module defines the EventListener interface"""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from events.event_listener import EventListener
from transaction.transaction import Transaction

class LoggingListener(EventListener):

    def update(sender: object) -> None:
        """Defines what happens to a sender object on event update
        
            Args:
                sender (Transaction): The sender object to notify on an update event
            Raises:
                TypeError: raised when
                    - sender is not a Transaction type
        """

        if isinstance(sender, Transaction):
            print(f"TRANSACTION PROCESSED\n{sender.__str__}")
        
        else:
            raise(TypeError("sender must be a Transaction type"))
        


