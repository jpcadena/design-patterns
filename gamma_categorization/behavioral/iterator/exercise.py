"""
A module for exercise in the gamma categorization.behavioral.iterator package.
"""
from typing import Any, Generator, Optional


class Node:
    """
    A Node class representing a node in a binary tree.
    Each node has a value, and optionally a left and/or right child.
    """

    def __init__(
        self,
        value: int,
        left: Optional['Node'] = None,
        right: Optional['Node'] = None,
    ) -> None:
        self.right: Optional['Node'] = right
        self.left: Optional['Node'] = left
        self.value: int = value
        self.parent: Optional['Node'] = None
        if left:
            left.parent = self
        if right:
            right.parent = self

    def traverse_preorder(self) -> Generator[int, Any, None]:
        """
        Traverse the tree in a preorder manner.
        :return: The value of the node in the order of traversal.
        :rtype: Generator[int, Any, None]
        """
        # Yield the value of the current node
        yield self.value
        # If there's a left child, recursively traverse its subtree
        if self.left:
            yield from self.left.traverse_preorder()
        # If there's a right child, recursively traverse its subtree
        if self.right:
            yield from self.right.traverse_preorder()
