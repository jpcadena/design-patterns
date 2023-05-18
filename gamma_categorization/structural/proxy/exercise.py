"""
Proxy Coding Exercise
"""


class Person:
    """
    Person clas
    """

    def __init__(self, age: int):
        self.age: int = age

    def drink(self) -> str:
        """
        The person drinks
        :return: Drinking
        :rtype: str
        """
        return "drinking"

    def drive(self) -> str:
        """
        The person drives
        :return: Driving
        :rtype: str
        """
        return "driving"

    def drink_and_drive(self) -> str:
        """
        The person drinks and drive
        :return: Driving while drunk
        :rtype: str
        """
        return "driving while drunk"


class ResponsiblePerson:
    """
    Responsible person class
    """

    def __init__(self, person: Person):
        self.person: Person = person

    @property
    def age(self) -> int:
        """
        Getter property for the age of the responsible person
        :return: The age
        :rtype: int
        """
        return self.person.age

    @age.setter
    def age(self, value: int) -> None:
        self.person.age = value

    def drink(self) -> str:
        """
        The responsible person drinks
        :return: Message validated
        :rtype: str
        """
        if self.person.age < 18:
            return "too young"
        return self.person.drink()

    def drive(self) -> str:
        """
        The responsible person drives
        :return: Message validated
        :rtype: str
        """
        if self.person.age < 16:
            return "too young"
        return self.person.drive()

    def drink_and_drive(self) -> str:
        """
        The responsible person dies
        :return: DEAD
        :rtype: str
        """
        return "dead"
