#!/usr/bin/python3
"Define class LockedClass"


def LockedClass:
    """
    prevent creation of new instance attributes, 
    except if the new instance attribute is called 'first_name'
    """

    __slots__ = ["first_name"]
