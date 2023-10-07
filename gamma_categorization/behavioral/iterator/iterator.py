"""
A module for iterator in the gamma categorization.behavioral.iterator package.
"""
from typing import Any, Generator, Optional, Self


class Node:
    """
    Tree node class representation
    """

    def __init__(
        self,
        value: int,
        left: Optional[Self] = None,
        right: Optional[Self] = None,
    ) -> None:
        self.right: Optional[Self] = right
        self.left: Optional[Self] = left
        self.value: int = value
        self.parent = None
        if left:
            left.parent = self
        if right:
            right.parent = self

    def __iter__(self) -> Generator['Node', None, None]:
        yield from traverse_in_order(self)


def traverse_in_order(current: Node) -> Generator[Node, Any, None]:
    """
    Traverse the tree in order
    :param current: The current node to traverse
    :type current: Node
    :return: Generator yielding nodes in order
    :rtype: Generator[Node, Any, None]
    """
    if current.left:
        yield from traverse_in_order(current.left)
    yield current
    if current.right:
        yield from traverse_in_order(current.right)


if __name__ == '__main__':
    #   1
    #  / \
    # 2   3

    # in-order: 213
    node: Node = Node(1, Node(2), Node(3))
    # Using the in-order generator directly
    for x in node:
        print(x.value)
