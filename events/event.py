"""This module defines the Event subject class for the logging system"""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from events.event_listener import EventListener

class Event():
    """This class represents an event which will notify all of its EventListeners"""

    def __init__(self):
        """Initializes an instance of the Event class"""

        self._listeners = []

    def add_listener(self, listener: EventListener) -> None:
        """Adds the given listener to the listeners list
        
            Args:
                listener (EventListener): The event listener to add to the 
                    listeners list.
        """

        self._listeners.append(listener)

    def remove_listener(self, listener: EventListener) -> None:
        """Removes the given listener from the listeners list
        
            Args:
                listener (EventListener): The event listener to remove from the
                    listeners list.
        """

        self._listeners.remove(listener)

    def notify(self, sender: object) -> None:
        """Evokes the event handler of every event listener in listeners to notify
            the given sender

            Args:
                sender (object): The sender of the event    
        """

        for listener in self._listeners:
            listener.update(sender)
        

