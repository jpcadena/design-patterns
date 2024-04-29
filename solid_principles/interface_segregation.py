"""
Interface Segregation Principle
"""

from abc import abstractmethod
from typing import Any


class Machine:
    """
    Machine class
    """

    def print(self, document: Any) -> None:
        """
        Print method
        :param document: The document to print
        :type document: Any
        :return: None
        :rtype: NoneType
        """
        raise NotImplementedError()

    def fax(self, document: Any) -> None:
        """
        Fax method
        :param document: The document to fax
        :type document: Any
        :return: None
        :rtype: NoneType
        """
        raise NotImplementedError()

    def scan(self, document: Any) -> None:
        """
        Scan method
        :param document: The document to scan
        :type document: Any
        :return: None
        :rtype: NoneType
        """
        raise NotImplementedError()


class MultiFunctionPrinter(Machine):
    """
    Multi Function Printer class
    """

    def print(self, document: Any) -> None:
        pass

    def fax(self, document: Any) -> None:
        pass

    def scan(self, document: Any) -> None:
        pass


class OldFashionedPrinter(Machine):
    """
    Old Fashioned Printer class based on Machine
    """

    def print(self, document: Any) -> None:
        # ok - print stuff
        pass

    def fax(self, document: Any) -> None:
        pass  # do-nothing

    def scan(self, document: Any) -> None:
        """Not supported!"""
        raise NotImplementedError("Printer cannot scan!")


class Printer:
    """
    Printer class
    """

    @abstractmethod
    def print(self, document: Any) -> None:
        """
        Print abstract method
        :param document: The document to print
        :type document: Any
        :return: None
        :rtype: NoneType
        """


class Scanner:
    """
    Scanner class
    """

    @abstractmethod
    def scan(self, document: Any) -> None:
        """
        Scan abstract method
        :param document: The document to scan
        :type document: Any
        :return: None
        :rtype: NoneType
        """


class MyPrinter(Printer):
    """
    My Printer class based on Printer
    """

    def print(self, document: Any) -> None:
        print(document)


class Photocopier(Printer, Scanner):
    """
    Photocopier class that inherits from Printer and Scanner
    """

    def print(self, document: Any) -> None:
        print(document)

    def scan(self, document: Any) -> None:
        pass  # something meaningful


class MultiFunctionDevice(Printer, Scanner):
    """
    MultiFunctionDevice class based on Printer and Scanner
    """

    @abstractmethod
    def print(self, document: Any) -> None:
        pass

    @abstractmethod
    def scan(self, document: Any) -> None:
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    """
    MultiFunctionMachine class based on MultiFunctionDevice
    """

    def __init__(self, printer: Printer, scanner: Scanner):
        self.printer: Printer = printer
        self.scanner: Scanner = scanner

    def print(self, document: Any) -> None:
        self.printer.print(document)

    def scan(self, document: Any) -> None:
        self.scanner.scan(document)


old_fashioned_printer = OldFashionedPrinter()
old_fashioned_printer.fax(123)  # nothing happens
old_fashioned_printer.scan(123)  # oops!
