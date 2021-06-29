"""
CC5- Trie
Name:chengming Wang
"""

from __future__ import annotations  # allow self-reference
import math


class TreeNode:
    """Tree Node that contains a value as well as left and right pointers"""
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right


def game_master(root: TreeNode) -> int:
    """
    para: root
    return the max sum
    """
    max_sum = 0
    def get_sum(node):
        """
        para:node,max_sum
        support function to get the max sum by binary
        """
        nonlocal  max_sum
        if not node:
            return True, 0, math.inf, -math.inf
        is_left, left_sum, left_min, left_max = get_sum(node.left)
        is_right, right_sum, right_min, right_max = get_sum(node.right)
        temp_sum = left_sum + right_sum + node.val
        if is_left and is_right and left_max < node.val < right_min:
            temp_max = right_max if right_max != -math.inf else node.val
            temp_min = left_min if left_min != math.inf else node.val
            max_sum = max(max_sum, temp_sum)
            return True, temp_sum, temp_min, temp_max
        return False, 0, None, None
    get_sum(root)
    return max_sum
