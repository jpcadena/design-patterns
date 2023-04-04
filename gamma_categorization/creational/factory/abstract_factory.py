"""
Abstract Factory
"""
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Type


class HotDrink(ABC):
    """
    Abstract class for Hot Drink
    """

    @abstractmethod
    def consume(self) -> None:
        """
        Consume method
        :return: None
        :rtype: NoneType
        """


class Tea(HotDrink):
    """
    Tea class that inherits from HotDrink
    """

    def consume(self) -> None:
        print("This tea is nice but I'd prefer it with milk")


class Coffee(HotDrink):
    """
    Coffee class that inherits from HotDrink
    """

    def consume(self) -> None:
        print('This coffee is delicious')


class HotDrinkFactory(ABC):
    """
    Hot Drink Factor abstract class
    """

    @abstractmethod
    def prepare(self, amount) -> HotDrink:
        """
        Abstract prepare method based on amount
        :param amount: Quantity to prepare
        :type amount: int
        :return: HotDrink instance
        :rtype: HotDrink
        """


class TeaFactory(HotDrinkFactory):
    """
    Tea Factory class that inherits from Hot Drink Factory
    """

    def prepare(self, amount) -> Tea:
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    """
    Coffee Factory class that inherits from Hot Drink Factory
    """

    def prepare(self, amount) -> Coffee:
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()


class HotDrinkMachine:
    """
    Hot Drink Machine class
    """

    class AvailableDrink(Enum):  # violates OCP
        """
        Available Drink that inherits from Enum
        """
        COFFEE = auto()
        TEA = auto()

    factories: dict[AvailableDrink, Type[CoffeeFactory | TeaFactory]] = {
        AvailableDrink.COFFEE: CoffeeFactory,
        AvailableDrink.TEA: TeaFactory
    }

    def __init__(self) -> None:
        self.factory_instances: dict = {
            drink: drink_factory() for drink, drink_factory in
            self.factories.items()}

    def make_drink(self) -> HotDrink:
        """
        Make drink from the Hot Drink Machine
        :return: HotDrink instance
        :rtype: HotDrink
        """
        print('Available drinks:')
        for index, drink in enumerate(self.factory_instances):
            print(f"{index}: {drink.name.title()}")
        drink_input: int = int(input(
            f'Please pick drink (0-{len(self.factory_instances) - 1}): '))
        amount: int = int(input('Specify amount: '))
        drink_enum = list(self.factory_instances.keys())[drink_input]
        return self.factory_instances[drink_enum].prepare(amount)


hot_drink_machine: HotDrinkMachine = HotDrinkMachine()
hot_drink: HotDrink = hot_drink_machine.make_drink()
hot_drink.consume()
