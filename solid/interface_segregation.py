"""
Interface Segregation Principle
"""
from abc import abstractmethod


class Machine:
    """
    Machine class
    """
    def print(self, document):
        """
        Print method
        :param document:
        :type document:
        :return: None
        :rtype: NoneType
        """
        raise NotImplementedError()

    def fax(self, document):
        """
        Fax method
        :param document:
        :type document:
        :return: None
        :rtype: NoneType
        """
        raise NotImplementedError()

    def scan(self, document):
        """
        Scan method
        :param document:
        :type document:
        :return: None
        :rtype: NoneType
        """
        raise NotImplementedError()


class MultiFunctionPrinter(Machine):
    """
    Multi Function Printer class
    """
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    """
    Old Fashioned Printer class based on Machine
    """

    def print(self, document):
        # ok - print stuff
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')


class Printer:
    """
    Printer class
    """

    @abstractmethod
    def print(self, document):
        """
        Print abstract method
        :param document: document
        :type document:
        :return: None
        :rtype: NoneType
        """


class Scanner:
    """
    Scanner class
    """

    @abstractmethod
    def scan(self, document):
        """
        Scan abstract method
        :param document: document
        :type document:
        :return:None
        :rtype: NoneType
        """


class MyPrinter(Printer):
    """
    My Printer class based on Printer
    """

    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    """
    Photocopier class that inherits from Printer and Scanner
    """

    def print(self, document):
        print(document)

    def scan(self, document):
        pass  # something meaningful


class MultiFunctionDevice(Printer, Scanner):
    """
    MultiFunctionDevice class based on Printer and Scanner
    """

    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    """
    MultiFunctionMachine class based on MultiFunctionDevice
    """

    def __init__(self, printer: Printer, scanner: Scanner):
        self.printer: Printer = printer
        self.scanner: Scanner = scanner

    def print(self, document) -> None:
        self.printer.print(document)

    def scan(self, document) -> None:
        self.scanner.scan(document)


old_fashioned_printer = OldFashionedPrinter()
old_fashioned_printer.fax(123)  # nothing happens
old_fashioned_printer.scan(123)  # oops!
