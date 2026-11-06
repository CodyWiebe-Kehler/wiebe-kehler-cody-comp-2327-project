
"""This module defines the EventListener interface"""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from events.event_listener import EventListener

class LoggingListener(EventListener):

    def update(self, sender: object) -> None:
        """Defines what happens to a sender object on event update
        
            Args:
                sender (Transaction): The sender object to notify on an update event
            Raises:
                TypeError: raised when
                    - sender is not a Transaction type
        """
        #import is in here to break circular import
        from transaction.transaction import Transaction

        if isinstance(sender, Transaction):
            print(f"TRANSACTION PROCESSED\n"
                  f"{50 * '='}\n"
                  f"{sender.__str__()}\n"
                  f"{50 * '-'}")
        
        else:
            #print(type(sender))
            raise(TypeError("sender must be a Transaction type"))
        


