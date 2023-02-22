"""
Factory Coding Exercise
Implement a PersonFactory that has a non-static create_person() method
 that takes a person's name and return a person initialized with this
  name and an id.
The id of the person should be set as a 0-based index of the object
 created.
So, the first person the factory makes should have Id=0, second Id=1
 and so on.
"""


class Person:
    """
    Person class
    """

    def __init__(self, person_id: int, name: str):
        self.person_id: int = person_id
        self.name: str = name


class PersonFactory:
    """
    Person factory class
    """

    def __init__(self):
        self.person_person_id: int = 0

    def create_person(self, name: str) -> Person:
        """
        Create a new person
        :param name: Name of the person
        :type name: str
        :return: Person instance
        :rtype: Person
        """
        person: Person = Person(self.person_person_id, name)
        self.person_person_id += 1
        return person


person_factory: PersonFactory = PersonFactory()
person_0: Person = person_factory.create_person('Tom')
person_1: Person = person_factory.create_person('Mark')
person_2: Person = person_factory.create_person('Travis')
