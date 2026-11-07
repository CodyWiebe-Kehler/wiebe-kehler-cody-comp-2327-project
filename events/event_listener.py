"""This module defines the EventListener interface"""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class EventListener(ABC):
    """The EventListener is an interface for all event listeners"""

    @abstractmethod
    def update(sender: object) -> None:
        """Defines what happens to a sender object on event update
        
            Args:
                sender (object): The sender object to notify on an update event
        """
        pass