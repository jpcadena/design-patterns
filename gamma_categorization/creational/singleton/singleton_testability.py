"""
Singleton Testability script
"""
import os
import unittest
from abc import ABC, ABCMeta, abstractmethod
from typing import Any


class IDatabase(ABC):
    """
    Shared interface for Database
    """

    @abstractmethod
    def __init__(self) -> None:
        pass

    @property
    @abstractmethod
    def population(self) -> dict[str, int]:
        """
        Population method for database
        :return: The population number
        :rtype: dict[str, int]
        """


class Singleton(ABCMeta):
    """
    Singleton class that inherits from type
    """

    _instances: dict[Any, Any] = {}

    def __call__(cls, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(IDatabase, metaclass=Singleton):
    """
    Database class that uses Singleton as its metaclass
    """

    def __init__(self) -> None:
        self._population: dict[str, int] = {}
        encoding: str = "utf-8"
        file_path: str = os.path.join(
            os.path.dirname(__file__), "..", "..", "..", "data", "capitals.txt"
        )
        try:
            with open(file_path, encoding=encoding) as file:
                lines: list[str] = [line.strip() for line in file]
                self._population = {
                    lines[i]: int(lines[i + 1]) for i in range(0, len(lines), 2)
                }
        except OSError:
            print("Could not read file:", file_path)

    @property
    def population(self) -> dict[str, int]:
        return self._population


class SingletonRecordFinder:
    """
    Singleton record finder class
    """

    @staticmethod
    def total_population(cities: list[str]) -> int:
        """
        Calculates the total population
        :param cities: List of cities
        :type cities: list[str]
        :return: Total population
        :rtype: int
        """
        result: int = 0
        for city in cities:
            result += Database().population[city]
        return result


class ConfigurableRecordFinder:
    """
    Configurable record finder class
    """

    def __init__(self, database: IDatabase) -> None:
        self.database: IDatabase = database

    def total_population(self, cities: list[str]) -> int:
        """
        Calculates total population
        :param cities: List of cities
        :type cities: list[str]
        :return: Total population
        :rtype: int
        """
        return sum(self.database.population[city] for city in cities)


class DummyDatabase(IDatabase):
    """
    Dummy database class
    """

    def __init__(self) -> None:
        self._population: dict[str, int] = {"alpha": 1, "beta": 2, "gamma": 3}

    @property
    def population(self) -> dict[str, int]:
        return self._population


class SingletonTests(unittest.TestCase):
    """
    Test class for Singleton that inherits from TestCase
    """

    ddb: DummyDatabase  # Provide type hint at the class level

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up class instance
        :return: None
        :rtype: NoneType
        """
        cls.ddb = DummyDatabase()

    def test_is_singleton(self) -> None:
        """
        Test function for is_singleton
        """
        db1: Database = Database()
        db2: Database = Database()
        self.assertTrue(db1 is db2)

    def test_singleton_total_population(self) -> None:
        """This tests on a live database :("""
        found_record: SingletonRecordFinder = SingletonRecordFinder()
        names: list[str] = ["Seoul", "Mexico City"]
        total_population: int = found_record.total_population(names)
        self.assertEqual(total_population, 17500000 + 17400000)

    def test_dependent_total_population(self) -> None:
        """
        Test function for dependent total population
        """
        crf: ConfigurableRecordFinder = ConfigurableRecordFinder(
            SingletonTests.ddb
        )
        self.assertEqual(crf.total_population(["alpha", "beta"]), 3)


if __name__ == "__main__":
    unittest.main()
