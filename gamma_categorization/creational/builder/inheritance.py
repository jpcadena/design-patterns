"""
Main script
"""


class Person:
    """
    Person class
    """

    def __init__(self) -> None:
        self.name: str = None
        self.position: str = None
        self.date_of_birth: str = None

    def __str__(self) -> str:
        return (
            f"{self.name} born on {self.date_of_birth} and works as"
            f" {self.position}"
        )

    @staticmethod
    def new():
        """
        Static method to create instance of Person
        :return: PersonBuilder instance
        :rtype: PersonBuilder
        """
        return PersonBuilder()


class PersonBuilder:
    """
    Person Builder class
    """

    def __init__(self) -> None:
        self.person: Person = Person()

    def build(self) -> Person:
        """
        Build a Person object
        :return: Person instance
        :rtype: Person
        """
        return self.person


class PersonInfoBuilder(PersonBuilder):
    """
    Person Info Builder class that inherits from Person Builder
    """

    def called(self, name: str):
        """
        Assign Name of person
        :param name: Name of person
        :type name: str
        :return: PersonInfoBuilder instance
        :rtype: PersonInfoBuilder
        """
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    """
    Person Job Builder class that inherits from Person Info Builder
    """

    def works_as_a(self, position: str):
        """
        Assign job position to person
        :param position: Position of person
        :type position: str
        :return: PersonJobBuilder instance
        :rtype: PersonJobBuilder
        """
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    """
    Person Birthdate Builder class that inherits from Person Job Builder
    """

    def born(self, date_of_birth: str):
        """
        Assign date of birth to person
        :param date_of_birth: Birthdate of person
        :type date_of_birth: str
        :return: PersonBirthDateBuilder instance
        :rtype: PersonBirthDateBuilder
        """
        self.person.date_of_birth = date_of_birth
        return self


person_birthdate_builder: PersonBirthDateBuilder = PersonBirthDateBuilder()
me: Person = (
    person_birthdate_builder.called("Dimitri")
    .works_as_a("Quant")
    .born("1/1/1980")
    .build()
)
print(me)
