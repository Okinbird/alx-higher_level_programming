#!/usr/bin/python3
"""
Defines an inherited list class MyList
"""


class MyList(list):
    """Implements sorted printing for the built-in list class"""
    
    def print_sorted(self):
        """Print a list in sorted ascenfing order"""
        print(sorted(self))
