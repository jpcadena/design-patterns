"""
A module for events in the gamma categorization.behavioral.observer package.
"""

from typing import Any


class Event(list[Any]):
    """
    A class for soccer events
    """

    def __call__(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        for item in self:
            item(*args, **kwargs)


class Person:
    """
    Person class represents a person with name and address
    """

    def __init__(self, name: str, address: str) -> None:
        self.name: str = name
        self.address: str = address
        self.falls_ill: Event = Event()

    def catch_a_cold(self) -> None:
        """
        Catch a cold event
        :return: None
        :rtype: NoneType
        """
        self.falls_ill(self.name, self.address)


def call_doctor(name: str, address: str) -> None:
    """
    Call a doctor to check vitals
    :param name: The name of the patient
    :type name: str
    :param address: The address where the sick person is
    :type address: str
        :return: None
        :rtype: NoneType
    """
    print(f"A doctor has been called to {address}")


if __name__ == "__main__":
    person = Person("Sherlock", "221B Baker St")
    person.falls_ill.append(lambda name, addr: print(f"{name} is ill"))
    person.falls_ill.append(call_doctor)
    person.catch_a_cold()
    # and you can remove subscriptions too
    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()
