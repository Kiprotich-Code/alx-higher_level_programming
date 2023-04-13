#!/usr/bin/python3
"Define class LockedClass"


def LockedClass:
    """
    prevent creation of new instance attributes, 
    except if the new instance attribute is called 'first_name'
    """

    _slots_ = ["first_name"]
