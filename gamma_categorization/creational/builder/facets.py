"""
Main script
"""
from typing import Any, Optional, Self


class Person:
    """
    Person class
    """

    def __init__(self) -> None:
        self.street_address: Optional[str] = None
        self.post_code: Optional[str] = None
        self.city: Optional[str] = None
        self.company_name: Optional[str] = None
        self.position: Optional[str] = None
        self.annual_income: Optional[int] = None

    def __str__(self) -> str:
        return (
            f"Address: {self.street_address}, {self.city} -"
            f" {self.post_code}.\n"
            f"Employed at: {self.company_name} as a {self.position},"
            f" earning {self.annual_income}"
        )


class PersonBuilder:  # facade
    """
    Builder class for Person
    """

    def __init__(self, person: Person = Person()) -> None:
        self.person: Person = person

    @property
    def lives(self) -> Any:
        """
        Property for living information of person
        :return: PersonAddressBuilder instance
        :rtype: PersonAddressBuilder
        """
        return PersonAddressBuilder(self.person)

    @property
    def works(self) -> Any:
        """
        Property for working information of person
        :return: PersonJobBuilder instance
        :rtype: PersonJobBuilder
        """
        return PersonJobBuilder(self.person)

    def build(self) -> Person:
        """
        Build method for Person Builder
        :return: Person instance
        :rtype: Person
        """
        return self.person


class PersonAddressBuilder(PersonBuilder):
    """
    Person Address Builder class inherited from Person Builder
    """

    def __init__(self, person: Person):
        super().__init__(person)

    def at(self, street_address: str) -> Self:
        """
        Assign Street Address for person
        :param street_address: Street Address for person
        :type street_address: str
        :return: PersonAddressBuilder instance
        :rtype: PersonAddressBuilder
        """
        self.person.street_address = street_address
        return self

    def with_post_code(self, post_code: str) -> Self:
        """
        Assign Post Code for person
        :param post_code: Post code for person
        :type post_code: str
        :return: PersonAddressBuilder instance
        :rtype: PersonAddressBuilder
        """
        self.person.post_code = post_code
        return self

    def in_city(self, city: str) -> Self:
        """
        Assign city for person
        :param city: City for person
        :type city: str
        :return: PersonAddressBuilder instance
        :rtype: PersonAddressBuilder
        """
        self.person.city = city
        return self


class PersonJobBuilder(PersonBuilder):
    """
    Person Job Builder class inherited from Person Builder
    """

    def __init__(self, person: Person):
        super().__init__(person)

    def at(self, company_name: str) -> Self:
        """
        Assign Company name for person
        :param company_name: Company name for person
        :type company_name: str
        :return: PersonJobBuilder instance
        :rtype: PersonJobBuilder
        """
        self.person.company_name = company_name
        return self

    def as_a(self, position: str) -> Self:
        """
        Assign Position for person at company
        :param position: Position for person
        :type position: str
        :return: PersonJobBuilder instance
        :rtype: PersonJobBuilder
        """
        self.person.position = position
        return self

    def earning(self, annual_income: int) -> Self:
        """
        Assign Annual income for person
        :param annual_income: Annual income for person
        :type annual_income: int
        :return: PersonJobBuilder instance
        :rtype: PersonJobBuilder
        """
        self.person.annual_income = annual_income
        return self


person_builder: PersonBuilder = PersonBuilder()
new_person = (
    person_builder.lives.at("123 London Road")
    .in_city("London")
    .with_post_code("SW12PC")
    .works.at("Fabrikam")
    .as_a("Engineer")
    .earning(123000)
    .build()
)
print(new_person)
