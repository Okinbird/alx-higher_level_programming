#!/usr/bin/python3
class LockedClass:
    """Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'
    """
    __slots__ = ['first_name']
