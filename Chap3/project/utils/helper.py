import sys
from .const_value import LOCATION


def getLocation():
    """get location from user input
    default beijing
    """
    user_input = sys.argv
    location = user_input[1] if len(user_input) >= 2 else LOCATION
    return location
