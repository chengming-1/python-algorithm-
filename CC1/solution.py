"""
Chengming Wang
Coding Challenge 1 - Sort of Sorted - Solution Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""
import string
def sort_of_sorted(subject):
    """
    Determine the longest sublist of strings in alphabetical order.
    :param data: [list] of strings in semi-sorted order
    :return: tuple containing
        [0]: [int] length of longest sorted sublist
        [1]: [list] longest sorted sublist of strings
    """
    if not subject:
        return 0, []
    times = 0
    result = [[subject[0]]]
    for i in range(1, len(subject)):
        if subject[i][0] < subject[i-1][0]:
            times += 1
            result.append([subject[i]])
        elif subject[i] == subject[i-1]:
            result[times].append(subject[i])
        elif subject[i][0] == subject[i-1][0]:
            if subject[i][1] < subject[i-1][1]:
                times += 1
                result.append([subject[i]])
            else:
                result[times].append(subject[i])
        else:
            result[times].append(subject[i])
    result = sorted(result, key=len, reverse=True)[0]
    return len(result), result
