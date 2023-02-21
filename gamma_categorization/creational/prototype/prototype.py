"""
Prototype script
"""
import copy


class Address:
    """
    Address class
    """

    def __init__(self, street_address: str, city: str, country: str) -> None:
        self.country: str = country
        self.city: str = city
        self.street_address: str = street_address

    def __str__(self) -> str:
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    """
    Person class
    """

    def __init__(self, name: str, address: str):
        self.name: str = name
        self.address: str = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


john: Person = Person("John", Address("123 London Road", "London", "UK"))
print(john)
# jane = john
jane = copy.deepcopy(john)
jane.name = "Jane"
jane.address.street_address = "124 London Road"
print(john, jane)
