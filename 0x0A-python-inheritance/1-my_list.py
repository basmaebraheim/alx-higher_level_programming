#!/usr/bin/python3
class MyList(list):
    """inherits from list"""
    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
