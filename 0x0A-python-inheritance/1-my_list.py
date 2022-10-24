#!/usr/bin/python3
"""
Defines an inherited list class MyList
"""


class MyList(list):
     """a subclass of list"""
     def __init__(self):
         """initializes the object"""
         super().__init__()
         
    def print_sorted(self):
        """Print a list in sorted ascenfing order"""
        print(sorted(self))
