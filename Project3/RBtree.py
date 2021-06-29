
from __future__ import annotations
from typing import TypeVar, Generic, Callable, Generator
from Project3.RBnode import RBnode as Node
from copy import deepcopy
import queue

T = TypeVar('T')


class RBtree:
    """
    A Red/Black Tree class
    :root: Root Node of the tree
    :size: Number of Nodes
    """

    __slots__ = ['root', 'size']

    def __init__(self, root: Node = None):
        """ Initializer for an RBtree """
        # this alllows us to initialize by copying an existing tree
        self.root = deepcopy(root)
        if self.root:
            self.root.parent = None
        self.size = 0 if not self.root else self.root.subtree_size()

    def __eq__(self, other: RBtree) -> bool:
        """ Equality Comparator for RBtrees """
        comp = lambda n1, n2: n1 == n2 and ((comp(n1.left, n2.left) and comp(n1.right, n2.right)) if (n1 and n2) else True)
        return comp(self.root, other.root) and self.size == other.size


    def __str__(self) -> str:
        """ represents Red/Black tree as string """

        if not self.root:
            return 'Empty RB Tree'

        root, bfs_queue, height = self.root, queue.SimpleQueue(), self.root.subtree_height()
        track = {i: [] for i in range(height + 1)}
        bfs_queue.put((root, 0, root.parent))

        while bfs_queue:
            n = bfs_queue.get()
            if n[1] > height:
                break
            track[n[1]].append(n)
            if n[0] is None:
                bfs_queue.put((None, n[1] + 1, None))
                bfs_queue.put((None, n[1] + 1, None))
                continue
            bfs_queue.put((None, n[1] + 1, None) if not n[0].left else (n[0].left, n[1] + 1, n[0]))
            bfs_queue.put((None, n[1] + 1, None) if not n[0].right else (n[0].right, n[1] + 1, n[0]))

        spaces = 12 * (2 ** (height))
        ans = '\n' + '\t\tVisual Level Order Traversal of RBtree'.center(spaces) + '\n\n'
        for i in range(height):
            ans += f"Level {i + 1}: "
            for n in track[i]:
                space = int(round(spaces / (2 ** i)))
                if not n[0]:
                    ans += ' ' * space
                    continue
                ans += "{} ({})".format(n[0], n[2].value if n[2] else None).center(space, " ")
            ans += '\n'
        return ans

    def __repr__(self) -> str:
        return self.__str__()

    ################################################################
    ################### Complete Functions Below ###################
    ################################################################

    ######################## Static Methods ########################
    # These methods are static as they operate only on nodes, without explicitly referencing an RBtree instance

    @staticmethod
    def set_child(parent: Node, child: Node, is_left: bool) -> None:
        """
        Insert Docstring here
        """
        if is_left is  True:
            parent.left = child
            child.parent = parent
        else:
            parent.right = child
            child.parent = parent

    #################################################################################
    @staticmethod
    def replace_child(parent: Node, current_child: Node, new_child: Node) -> None:
        """
        Insert Docstring here
        """
        if parent.left == current_child:
            parent.left = new_child
        else:
            parent.right = new_child

    #################################################################################
    @staticmethod
    def get_sibling(node: Node) -> Node:
        """
        Insert Docstring here
        """
        if node.parent is None:
            return None
        if node.parent.left == node:
            return node.parent.right
        return node.parent.left

    #################################################################################
    @staticmethod
    def get_grandparent(node: Node) -> Node:
        """
        Insert Docstring here
        """
        if node.parent is None:
            return None
        if node.parent.parent is None:
            return None
        return node.parent.parent

    #################################################################################
    @staticmethod
    def get_uncle(node: Node) -> Node:
        """
        Insert Docstring here
        """
        if node is None or node.parent is None:
            return None
        return RBtree.get_sibling(node.parent)

    #################################################################################
    ######################## Misc Utilities ##########################

    def min(self, node: Node) -> Node:
        """
        Insert Docstring here
        """
        if node is None:
            return None
        if node.left is None:
            return node
        leftNode = node.left
        while leftNode.left != None:
            leftNode = leftNode.left
        return leftNode
    #################################################################################
    def max(self, node: Node) -> Node:
        """
        Insert Docstring here
        """
        if node is None:
            return None
        if node.right is None:
            return node
        rightNode = node.right
        while rightNode.right != None:
            rightNode = rightNode.right
        return rightNode

    #################################################################################
    def search(self, node: Node, val: Generic[T]) -> Node:
        """
        Insert Docstring here
        """
        if node is None or val == node.value:
            return node

        if val < node.value:
            if node.left.value < val and node.left.right is None:
                return node.left
            if val < node.left.value and node.left.left is None:
                return node.left
            return self.search(node.left, val)

        if node.left.value < val and node.left.right is None:
            return node.left
        if val < node.left.value and node.left.left is None:
            return node.left
        return self.search(node.right, val)

    ######################## Tree Traversals #########################

    def inorder(self, node: Node) -> Generator[Node, None, None]:
        """
        Insert Docstring here
        """
        if node != None:
            self.inorder(node.left)
            print(node, " ")
            self.inorder(node.right)

    #################################################################################
    def preorder(self, node: Node) -> Generator[Node, None, None]:
        """
        Insert Docstring here
        """
        if node != None:
            print(node, " ")
            self.preorder(node.left)
            self.preorder(node.right)

    #################################################################################
    def postorder(self, node: Node) -> Generator[Node, None, None]:
        """
        Insert Docstring here
        """
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node, " ")

    #################################################################################
    def bfs(self, node: Node) -> Generator[Node, None, None]:
        """
        Insert Docstring here
        """

    ################### Rebalancing Utilities ######################

    def left_rotate(self, node: Node) -> None:
        """
        Insert Docstring here
        """
        rightNode = node.right
        node.right = rightNode.left
        if rightNode.left != None:
            rightNode.left.parent = node

        rightNode.parent = node.parent
        if node.parent is None:
            self.root = rightNode
        elif node == node.parent.left:
            node.parent.left = rightNode
        else:
            node.parent.right = rightNode
        rightNode.left = node
        node.parent = rightNode

    #################################################################################
    def right_rotate(self, node: Node) -> None:
        """
        Insert Docstring here
        """
        leftNode = node.left
        node.left = leftNode.right
        if leftNode.right != None:
            leftNode.right.parent = node

        leftNode.parent = node.parent
        if node.parent is None:
            self.root = leftNode
        elif node == node.parent.right:
            node.parent.right = leftNode
        else:
            node.parent.left = leftNode
        leftNode.right = node
        node.parent = leftNode

    #################################################################################
    def insertion_repair(self, node: Node) -> None:
        """
        Insert Docstring here
        """
        while node.parent.is_red:
            if node.parent == node.parent.parent.right:
                uncleNode = self.get_uncle(node)
                if uncleNode.is_red:
                    uncleNode.is_red = False
                    node.parent.is_red = False
                    node.parent.parent.is_red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.is_red = False
                    node.parent.parent.is_red = True
                    self.left_rotate(node.parent.parent)
            else:
                uncleNode = self.get_uncle(node)

                if uncleNode.is_red:
                    uncleNode.is_red = False
                    node.parent.is_red = False
                    node.parent.parent.is_red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.is_red = False
                    node.parent.parent.is_red = True
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.is_red = False

    #################################################################################
    def prepare_removal(self, node: Node) -> None:
        """
        Insert Docstring here
        """
        while node != self.root and node.is_red is False:
            if node == node.parent.left:
                sNode = node.parent.right
                if sNode.is_red is True:
                    sNode.is_red = False
                    node.parent.is_red = True
                    self.left_rotate(node.parent)
                    sNode = node.parent.right

                if sNode.left.is_red is False and sNode.right.is_red is False:
                    sNode.is_red = True
                    node = node.parent
                else:
                    if sNode.right.is_red is False:
                        sNode.left.is_red = False
                        sNode.is_red = True
                        self.right_rotate(sNode)
                        sNode = node.parent.right

                    sNode.is_red = node.parent.is_red
                    node.parent.is_red = False
                    sNode.right.is_red = False
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                sNode = node.parent.left
                if sNode.is_red is True:
                    sNode.is_red = False
                    node.parent.is_red = True
                    self.right_rotate(node.parent)
                    sNode = node.parent.left

                if sNode.right.is_red is False and sNode.right.is_red is False:
                    sNode.is_red = True
                    node = node.parent
                else:
                    if sNode.left.is_red is False:
                        sNode.right.is_red = False
                        sNode.is_red = True
                        self.left_rotate(sNode)
                        sNode = node.parent.left

                    sNode.is_red = node.parent.is_red
                    node.parent.is_red = False
                    sNode.left.is_red = False
                    self.right_rotate(node.parent)
                    node = self.root
        node.is_red = False

    ##################### Insertion and Removal #########################

    def insert(self, node: Node, val: Generic[T]) -> None:
        """
        Insert Docstring here
        """
        newNode = Node(val)
        yNode = None
        xNode = Node


        while xNode != None:
            yNode = xNode
            if newNode.value < xNode.value:
                xNode = xNode.left
            else:
                xNode = xNode.right


        newNode.parent = yNode
        if yNode is None:
            node = newNode
        elif newNode.value < yNode.value:
            yNode.left = newNode
        else:
            yNode.right = newNode

        if newNode.parent is None:
            newNode.is_red = False
            return

        if newNode.parent.parent is None:
            return

        self.insertion_repair(newNode)

    #################################################################################
    def remove(self, node: Node, val: Generic[T]) -> None:
        """
        Insert Docstring here
        """
        tempNode = None
        while node != None:
            if node.value == val:
                tempNode = node

            if node.value <= val:
                node = node.right
            else:
                node = node.left

        if tempNode is None:
            return

        tempNode2 = tempNode
        redColor = tempNode2.is_red
        if tempNode.left is None:
            tempNode3 = tempNode.right
            if tempNode.parent is None:
                self.root = tempNode.right
            elif tempNode == tempNode.parent.left:
                tempNode.parent.left = tempNode.right
            else:
                tempNode.parent.right = tempNode.right
            tempNode.right.parent = tempNode.parent
        elif tempNode.right is None:
            tempNode3 = tempNode.left
            if tempNode.parent is None:
                self.root = tempNode.left
            elif tempNode == tempNode.parent.left:
                tempNode.parent.left = tempNode.left
            else:
                tempNode.parent.right = tempNode.left
            tempNode.left.parent = tempNode.parent
        else:
            tempNode2 = self.min(tempNode.right)
            redColor = tempNode2.is_red
            tempNode3 = tempNode2.right
            if tempNode2.parent == tempNode:
                if tempNode3 != None:
                    tempNode3.parent = tempNode2
            else:
                if tempNode2.parent is None:
                    self.root = tempNode2.right
                elif tempNode2 == tempNode2.parent.left:
                    tempNode2.parent.left = tempNode2.right
                else:
                    tempNode2.parent.right = tempNode2.right
                tempNode2.right.parent = tempNode2.parent
                tempNode2.right = tempNode.right
                tempNode2.right.parent = tempNode2

            if tempNode.parent is None:
                self.root = tempNode2
            elif tempNode == tempNode.parent.left:
                tempNode.parent.left = tempNode2
            else:
                tempNode.parent.right = tempNode2
            tempNode2.parent = tempNode.parent
            tempNode2.left = tempNode.left
            tempNode2.left.parent = tempNode2
            tempNode2.is_red = tempNode.is_red
        if redColor is False:
            self.prepare_removal(tempNode3)
