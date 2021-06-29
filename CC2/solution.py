"""
Chengming Wang
Coding Challenge 2 - Drop It Like It's Hot - Solution
CSE 331 Fall 2020
Professor Sebnem Onsay
"""


def firefighter(grid, k):
    """
    Given an n x n 2D list of 0's and 1's and an integer k, determine the greatest number of 1's
    that can be covered by a square of size k x k. Return a tuple (a, b, c) where
        a = number of 1's this optimal k x k square covers
        b = the row of the top left corner of this square
        c = the col of the top left corner of this square
    :param grid: [list[list[int]]] a square 2D list of 0, 1 integers
    :param k: [int] the size of the square placed to cover 1's
    :return: [tuple[int, int, int]] a tuple (a, b, c) where
        a = number of 1's this optimal k x k square covers
        b = the row of the top left corner of this square
        c = the col of the top left corner of this square
    """
    count = 0
    row = 0
    col = 0
    for i in range(0, len(grid) - k + 1):
        for j in range(0, len(grid[0]) - k + 1):
            total = 0
            for grid_ro in range(i, i + k):
                for grid_co in range(j, j + k):
                    total = total + grid[grid_ro][grid_co]
            if total > count:
                count = total
                row = i
                col = j
    return count, row, col
