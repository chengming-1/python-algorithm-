"""
Name:
CC4 - Starter Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""


# You must add insert(), remove() and shortest_book() as defined by the specs.
# Don't forget docstrings!
class Books:
    def __init__(self):
        '''
        :param self:init the list
        '''
        self._item = []

    def is_empty(self):
        '''
        check it's empty or not
        '''
        return len(self._item) == 0

    def insert(self, num):
        '''
        :param num: the num to insert
        '''
        self._item.append(num)

    def remove(self):
        '''
        remove the final element
        '''
        if self.is_empty():
            return None
        return self._item.pop()

    def shortest_book(self):
        '''
        find the smallest element
        '''
        if self.is_empty():
            return None
        return min(self._item)
