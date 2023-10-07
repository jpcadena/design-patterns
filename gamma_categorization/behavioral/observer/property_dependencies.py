"""
A module for property dependencies in the gamma
 categorization.behavioral.observer package.
"""
from gamma_categorization.behavioral.observer.property_observers import (
    PropertyObservable,
)


class Person(PropertyObservable):
    def __init__(self, age: int = 0):
        super().__init__()
        self._age: int = age

    @property
    def age(self) -> int:
        """
        The age of the person property
        :return: The age of the person
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if self._age == value:
            return
        old_can_vote: bool = self.can_vote
        self._age = value
        self.property_changed('age', value)
        if old_can_vote != self.can_vote:
            self.property_changed('can_vote', self.can_vote)

    @property
    def can_vote(self) -> bool:
        """
        Validate if the person can vote
        :return: True if the person's age is greater or equals than 18;
         False otherwise
        :rtype: bool
        """
        return self._age >= 18


if __name__ == '__main__':

    def person_changed(name: str, value: bool) -> None:
        """
        Check if the person has changed its status to vote
        :param name: The name of the person
        :type name: str
        :param value: The status of the person to vote
        :type value: bool
        :return: None
        :rtype: NoneType
        """
        if name == 'can_vote':
            print(f'Voting status changed to {value}')

    person: Person = Person()
    person.property_changed.append(person_changed)

    for some_age in range(16, 21):
        print(f'Changing age to {some_age}')
        person.age = some_age
