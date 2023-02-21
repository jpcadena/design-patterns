"""
Abstract Factory
"""
from abc import ABC, abstractmethod
from enum import Enum, auto


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
    def prepare(self, amount) -> None:
        """
        Abstract prepare method based on amount
        :param amount: Quantity to prepare
        :type amount: int
        :return: None
        :rtype: NoneType
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

    factories: list[tuple[str, HotDrinkFactory]] = []
    initialized = False

    def __init__(self) -> None:
        if not self.initialized:
            self.initialized = True
            for available_drink in self.AvailableDrink:
                name: str = available_drink.name.title()
                factory_name: str = name + 'Factory'
                factory_instance: HotDrinkFactory = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self) -> HotDrink:
        """
        Make drink from the Hot Drink Machine
        :return: HotDrink instance
        :rtype: HotDrink
        """
        print('Available drinks:')
        for factory in self.factories:
            print(factory[0])
        drink_input: int = int(input(
            f'Please pick drink (0-{len(self.factories) - 1}): '))
        amount: int = int(input('Specify amount: '))
        return self.factories[drink_input][1].prepare(amount)


hot_drink_machine: HotDrinkMachine = HotDrinkMachine()
hot_drink: HotDrink = hot_drink_machine.make_drink()
hot_drink.consume()
