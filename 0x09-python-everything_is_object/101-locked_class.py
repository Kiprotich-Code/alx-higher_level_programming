#!/usr/bin/python3
"Define class LockedClass."


class LockedClass:
    """
    Prevent creation of new instance attributes, except if the new instance attribute is called 'first_name'.
    """

    __slots__ = ["first_name"]
