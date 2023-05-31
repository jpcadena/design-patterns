"""
Singleton Testability script
"""
import os
import unittest
from typing import Any


class Singleton(type):
    """
    Singleton class that inherits from type
    """

    _instances: dict[Any, Any] = {}

    def __call__(cls, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]


class Database(metaclass=Singleton):
    """
    Database class that uses Singleton as its metaclass
    """

    def __init__(self) -> None:
        self.population: dict[str, int] = {}
        encoding: str = "utf-8"
        file_path: str = os.path.join(
            os.path.dirname(__file__), "..", "..", "..", "data", "capitals.txt"
        )
        try:
            with open(file_path, "r", encoding=encoding) as file:
                lines: list[str] = [line.strip() for line in file]
                self.population = {
                    lines[i]: int(lines[i + 1]) for i in
                    range(0, len(lines), 2)
                }
        except IOError:
            print("Could not read file:", file_path)


class SingletonRecordFinder:
    """
    Singleton record finder class
    """

    def total_population(self, cities: list[str]) -> int:
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

    def __init__(self, database: Database) -> None:
        self.database: Database = database

    def total_population(self, cities: list[str]) -> int:
        """
        Calculates total population
        :param cities: List of cities
        :type cities: list[str]
        :return: Total population
        :rtype: int
        """
        return sum(self.database.population[city] for city in cities)


class DummyDatabase:
    """
    Dummy database class
    """

    population: dict[str, int] = {"alpha": 1, "beta": 2, "gamma": 3}

    def get_population(self, name: str) -> int:
        """
        Get population
        :param name: The name of the population
        :type name: str
        :return: The population
        :rtype: int
        """
        return self.population[name]


class SingletonTests(unittest.TestCase):
    """
    Test class for Singleton that inherits from TestCase
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.ddb = DummyDatabase()

    def test_is_singleton(self) -> None:
        """
        Test function for is_singleton
        :return:
        :rtype:
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
        # what if these change?

    def test_dependent_total_population(self) -> None:
        """
        Test function for dependent total population
        :return: None
        :rtype: NoneType
        """
        crf: ConfigurableRecordFinder = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(crf.total_population(["alpha", "beta"]), 3)


if __name__ == "__main__":
    unittest.main()
