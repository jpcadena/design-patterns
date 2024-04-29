"""
Singleton Coding Exercise
Write a function called is_singleton().
This method takes a factory method that returns an object, and it's up
 to you to determine whether that object is a singleton instance.
"""

from typing import Any, Callable


def is_singleton(factory: Callable[[], Any]) -> bool:
    """
    Checks if the object returned by the factory method is a singleton
     instance
    :param factory: Factory method that returns an object
    :type factory: Callable
    :return: True if the object returned by the factory method is a
     singleton instance, False otherwise
    :rtype: bool
    """
    obj1 = factory()
    obj2 = factory()
    return obj1 is obj2
