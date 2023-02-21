"""
Prototype Factory script
"""
import copy


class Address:
    """
    Address class
    """

    def __init__(self, street_address: str, suite: int, city: str) -> None:
        self.street_address: str = street_address
        self.suite: int = suite
        self.city: str = city

    def __str__(self) -> str:
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'


class Employee:
    """
    Employee class
    """

    def __init__(self, name, address) -> None:
        self.name: str = name
        self.address: str = address

    def __str__(self) -> str:
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    """
    Employee Factory class
    """
    main_office_employee: Employee = Employee(
        "", Address("123 East Dr", 0, "London"))
    aux_office_employee: Employee = Employee(
        "", Address("123B East Dr", 0, "London"))

    @staticmethod
    def __new_employee(proto: Employee, name: str, suite: int) -> Employee:
        result: Employee = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name: str, suite: int) -> Employee:
        """
        Create a new employee at main office
        :param name: Name of the employee
        :type name: str
        :param suite: Number of the suite
        :type suite: int
        :return: Employee instance
        :rtype: Employee
        """
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_office_employee(name: str, suite: int) -> Employee:
        """
        Create a new employee at aux office
        :param name: Name of the employee
        :type name: str
        :param suite: Number of the suite
        :type suite: int
        :return: Employee instance
        :rtype: Employee
        """
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suite
        )


# main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
# aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))

# john = copy.deepcopy(main_office_employee)
# john.name = "John"
# john.address.suite = 101
# print(john)

# would prefer to write just one line of code
jane: Employee = EmployeeFactory.new_aux_office_employee("Jane", 200)
print(jane)
