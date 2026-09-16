from enum import Enum

class AccountStatus(Enum):
    """This enumeration represents the possible status' of a bank account"""

    INACTIVE = 0
    """The inactive account status"""

    ACTIVE = 1
    """The active account status"""

    SUSPENDED = 2
    """The suspended account status"""

    CLOSED = 3
    """The closed account status"""