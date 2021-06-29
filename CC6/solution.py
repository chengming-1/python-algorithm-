"""
CC6 - It's As Easy As 01-10-11
Name: Chengming Wang
"""

from typing import Generator, Any


class Node:
    """
    Node Class
    :value: stored value
    :next: reference to next node
    """

    def __init__(self, value) -> None:
        """
        Initializes the Node class
        """
        self.value: str = value
        self.next: Node = None

    def __str__(self) -> str:
        return self.value


class Queue:
    """
    Queue Class
    :first: reference to first node in the queue
    :last: reference to last node in the queue
    """

    def __init__(self) -> None:
        """
        Initializes the Queue class
        """
        self.first: Node = None
        self.last: Node = None

    def __str__(self) -> str:
        final = ''
        current = self.first
        final += ''
        while current is not None:
            final += str(current) + '    '
            current = current.next
        final += ''
        return final

    def insert(self, value: str) -> None:
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def pop(self):
        if not self.first:
            return None
        temp = self.first
        self.first = self.first.next
        temp = None
        return self.first


def alien_communicator(n: Any) -> Generator[str, None, None]:
    q = Queue()
    q.insert("")
    def cal(x):
        neg = False
        s = ""
        if x == 0:
            return "0"
        neg = x < 0
        if neg:
            x = -1 * x
        while x != 0:
            s = str(x % 2) + s
            x = int(x / 2)
        if neg:
            s = "-".s
        return s
    for i in range(0, n + 1):
        q.insert(q.first.value+cal(i))
        q.pop()
    return q



