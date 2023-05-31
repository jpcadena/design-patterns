"""
Dependency Inversion Principle
"""
from abc import abstractmethod
from enum import Enum
from typing import Any, Generator


class Relationship(int, Enum):
    """
    Relationship class based on Enum
    """

    PARENT: int = 0
    CHILD: int = 1
    SIBLING: int = 2


class Person:
    """
    Person class with name
    """

    def __init__(self, name: str):
        self.name: str = name


class RelationshipBrowser:
    """
    Relationship Browser class
    """

    @abstractmethod
    def find_all_children_of(self, name: str) -> Any:
        """
        Find all children of parent name
        :param name: parent
        :type name: str
        :return: None
        :rtype: NoneType
        """


class Relationships(RelationshipBrowser):
    """
    Low-level Relationship Browser class
    """

    relations: list[tuple[Person, Enum, Person]] = []

    def add_parent_and_child(self, parent: Person, child: Person) -> None:
        """
        Add parent and child relationship
        :param parent: parent object
        :type parent: Person
        :param child: child object
        :type child: Person
        :return: None
        :rtype: NoneType
        """
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))

    def find_all_children_of(self, name: str) -> Generator[str, None, None]:
        for relationship in self.relations:
            if (
                relationship[0].name == name
                and relationship[1] == Relationship.PARENT
            ):
                yield relationship[2].name


class Research:
    """
    Research class
    """

    # dependency on a low-level module directly
    # bad because strongly dependent on e.g. storage type

    # def __init__(self, relationships):
    #     # high-level: find all of John's children
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, browser: RelationshipBrowser) -> None:
        for parent in browser.find_all_children_of("John"):
            print(f"John has a child called {parent}")


my_parent: Person = Person("John")
child1: Person = Person("Chris")
child2: Person = Person("Matt")

# low-level module
relationships: Relationships = Relationships()
relationships.add_parent_and_child(my_parent, child1)
relationships.add_parent_and_child(my_parent, child2)

Research(relationships)
