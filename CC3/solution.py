"""
Name:Chengming Wang
CC3 - Starter Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""

def find_missing_value(list):
    """
    :param list: list
    :return: the lacking number
    """
    if len(list) == 0: # if is empty
        return 0
    if list[len(list) - 1] != len(list):# if lack the last one
        return len(list)
    def find_missing_value_recursive(start, end):
        """
        :param list: beginning and ending of list
        :return: the lacking number
        helper recurrence function
        get middle number and use it for binary search
        """
        if start >= end:
            return 0
        middle = (end + start)//2
        if middle > 0 and list[middle] - list[middle - 1] != 1:
            return list[middle] - 1
        if list[middle + 1] - list[middle] != 1:
            return list[middle] + 1
        if list[middle] == list[0] + middle:
            return find_missing_value_recursive(middle + 1, end)
        return find_missing_value_recursive(start, middle-1)
    return find_missing_value_recursive(0, len(list)-1)
