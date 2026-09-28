"""This module defines the enumeration for the possible status' of a transaction"""
from enum import Enum

class TransactionStatus(Enum):
    """This enumeration represents the possible status' of a transaction"""

    PENDING = 1
    """The Pending transaction status"""

    PROCESSED = 2
    """The Pending transaction status"""

    FAILED = 3
    """The Pending transaction status"""