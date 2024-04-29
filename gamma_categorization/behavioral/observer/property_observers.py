"""
A module for property observers in the gamma categorization.behavioral.observer
 package.
"""

from gamma_categorization.behavioral.observer.events import Event


class PropertyObservable:
    """
    Property Observable class representation
    """

    def __init__(self) -> None:
        self.property_changed: Event = Event()


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
        self._age = value
        self.property_changed("age", value)


class TrafficAuthority:
    """
    Traffic Authority class representation
    """

    def __init__(self, person: Person):
        self.person: Person = person
        person.property_changed.append(self.person_changed)

    def person_changed(self, name: str, value: int) -> None:
        """
        Person changed property to validate driving
        :param name: The name of the person
        :type name: str
        :param value: The age of the person
        :type value: int
        :return: None
        :rtype: NoneType
        """
        if name == "age":
            if value < 16:
                print("Sorry, you still cannot drive")
            else:
                print("Okay, you can drive now")
                self.person.property_changed.remove(self.person_changed)


if __name__ == "__main__":
    some_person: Person = Person()
    traffic_authority: TrafficAuthority = TrafficAuthority(some_person)
    for some_age in range(14, 20):
        print(f"Setting age to {some_age}")
        some_person.age = some_age
