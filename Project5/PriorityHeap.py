
from typing import List, Tuple, Any


class Node:
    """
    Node definition should not be changed in any way
    """
    __slots__ = ['key', 'value']

    def __init__(self, k: Any, v: Any):
        """
        Initializes node
        :param k: key to be stored in the node
        :param v: value to be stored in the node
        """
        self.key = k
        self.value = v

    def __lt__(self, other):
        """
        Less than comparator
        :param other: second node to be compared to
        :return: True if the node is less than other, False if otherwise
        """
        return self.key < other.key or (self.key == other.key and self.value < other.value)

    def __gt__(self, other):
        """
        Greater than comparator
        :param other: second node to be compared to
        :return: True if the node is greater than other, False if otherwise
        """
        return self.key > other.key or (self.key == other.key and self.value > other.value)

    def __eq__(self, other):
        """
        Equality comparator
        :param other: second node to be compared to
        :return: True if the nodes are equal, False if otherwise
        """
        return self.key == other.key and self.value == other.value

    def __str__(self):
        """
        Converts node to a string
        :return: string representation of node
        """
        return '({0}, {1})'.format(self.key, self.value)

    __repr__ = __str__


class PriorityQueue:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = []

    def __str__(self) -> str:
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data)

    __repr__ = __str__

    def to_tree_format_string(self) -> str:
        """
        Prints heap in Breadth First Ordering Format
        :return: String to print
        """
        string = ""
        # level spacing - init
        nodes_on_level = 0
        level_limit = 1
        spaces = 10 * int(1 + len(self))

        for i in range(len(self)):
            space = spaces // level_limit
            # determine spacing

            # add node to str and add spacing
            string += str(self.data[i]).center(space, ' ')

            # check if moving to next level
            nodes_on_level += 1
            if nodes_on_level == level_limit:
                string += '\n'
                level_limit *= 2
                nodes_on_level = 0
            i += 1

        return string

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def __len__(self) -> int:
        """
        Method to find the length or number of elements currenlty in the queue
        :return: int representation of the length
        """
        return len(self.data)

    def empty(self) -> bool:
        """
        Method to check if the queue is currenlty empty or the size of the queue is 0
        :return: boolean flag, true if queue is empty or false if it is not
        """
        if len(self.data) == 0:
            return True
        return False

    def top(self) -> Node:
        """
        Method to find the root element of the heap tree
        0 is the topmost element
        :return: The Node element at index 0
        """
        if len(self.data) > 0:
            return self.data[0]
        return None

    def get_left_child_index(self, index: int) -> int:
        """
        Method to get the left child of a node in tree representation of the heap.
        :param index: index is the integer number of the index in list of  left child index
        :return: index of the left child as integer
        """
        if len(self.data) > (index * 2) + 1:
            return (index * 2) + 1
        return None


    def get_right_child_index(self, index: int) -> int:
        """
        Method to get the right child of a node in tree representation of the heap.
        :param index:integer number of the index in list of nodes whose right child index
        should be returned
        :return: index of the right child as integer
        """
        if len(self.data) > (index * 2) + 2:
            return (index * 2) + 2
        return None

    def get_parent_index(self, index: int) -> int:
        """
        Returns the index of parent node for the given index of a node
        :param index: integer number of the index of a node whose parent index is required
        :return: index of the parent node
        """
        if (index >= 1) and (index <= len(self.data)):
            return (index - 1) // 2
        return None

    def push(self, key: Any, val: Any) -> None:
        """
        to append a new element in the queue
        locatin to maintain the mean heap
        :param key: Key of the Node
        :param val: Value of the Node
        """
        self.data.append(Node(key, val))
        self.percolate_up(len(self.data) - 1)

    def pop(self) -> Node:
        """
        MEthod to remove the element with least priority,
        after removing the element structure is rearranged to maintain the min heap property
        :return: Node with least prioroty at index 0
        """
        # Equal to 1 since the heap list was initialized with a value
        root = self.top()
        if root is None:
            return
        if len(self.data) == 1:
            self.data = []
            return root
        # Get root of the heap (The min value of the heap)
        root = self.data[0]
        # Move the last value of the heap to the root
        self.data[0] = self.data[self.__len__()-1]
        # Pop the last value since a copy was set on the root
        *self.data, _ = self.data
        # Move down the root (value at index 1) to keep the heap property
        self.percolate_down(0)
        # Return the min value of the heap
        return root

    def get_min_child_index(self, index: int) -> int:
        """
        Method to find out the index of minimum child out of left and right child of an element
        :param index: int index of the element whose minimum child index is required
        :return: int index of the left or right child according to the comparison
        """
        if self.get_right_child_index(index) is None:
            return self.get_left_child_index(index)
        if self.data[self.get_left_child_index(index)].__lt__(self.data[self.get_right_child_index(index)]):
            return self.get_left_child_index(index)
        else:
            return self.get_right_child_index(index)

    def percolate_up(self, index: int) -> None:
        """
        Method to move an element up in the tree according to its priority
        :param index: int index of the element which needs to be moved
        """
        if index > 0:
            # While the element is not the root or the left element
            while True:
                # If the element is less than its parent swap the elements
                if self.data[index].__lt__(self.data[self.get_parent_index(index)]):
                    self.data[index], self.data[self.get_parent_index(index)] = self.data[self.get_parent_index(index)], \
                                                                                self.data[index]
                else:
                    break
                # Move the index to the parent to keep the properties
                index = self.get_parent_index(index)
                if index == 0:
                    break

    def percolate_down(self, index: int) -> None:
        """
        Method to move an element down in the tree according to its priority
        :param index: int index of the element which needs to be moved
        """
        # if the current node has at least one child
        while self.get_left_child_index(index) is not None:
            # Get the index of the min child of the current node
            mc = self.get_min_child_index(index)
            # Swap the values of the current element is greater than its min child
            if self.data[index].__gt__(self.data[mc]):
                self.data[index], self.data[mc] = self.data[mc], self.data[index]
            else:
                break
            index = mc


class MaxHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = PriorityQueue()

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data.data)

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self.data)

    def print_tree_format(self):
        """
        Prints heap in bfs format
        """
        self.data.tree_format()

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def empty(self) -> bool:
        """
        Method to check if the heap is empty or its size is 0
        :return: int value representing the number of elements in the heap
        """
        return self.data.empty()

    def top(self) -> int:
        """
        get the topmost element in max heap
        :return: int value at index 0 of list
        """
        if self.data.top() is None:
            return None
        return abs(self.data.top().key)

    def push(self, key: int) -> None:
        """
        Method to add a new value to the heap
        :param key: int key of the new element
        """
        self.data.push(-key, 0)

    def pop(self) -> int:
        """
        Method to remove the element with highest priority
        element is at the index 0 rearranged to maintain its prop
        """
        return abs(self.data.pop().key)


def heap_sort(array):
    """
    Method to sort a given array in ascending order using max heap
    :param array: the array or list that needs to be sorted
    :return: the sorted array
    """
    heap = MaxHeap()
    for i in array:
        heap.push(i)
    for i in range(len(array)-1, -1, -1):
        array[i] = heap.pop()
    return array


def find_ranking(rank, results: List[Tuple[int, str]]) -> str:
    """
    The method to find the ranking or element with given prioroty in a list
    :param rank: Rank or the priority of element
    :param results: The list in which priority is to be found
    :return: The value of given rank or priority
    """
    queue = PriorityQueue()
    for tup in results:
        queue.push(tup[0], tup[1])
    if rank <= queue.__len__():
        for _ in range(rank-1):
            queue.pop()
        return queue.top().value
    return None
