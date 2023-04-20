"""
Protection Proxy script
"""


class Driver:
    """
    Driver class
    """

    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age


class Car:
    """
    Car class
    """

    def __init__(self, driver: Driver):
        self.driver: Driver = driver

    def drive(self) -> None:
        """
        Drive method
        :return: None
        :rtype: NoneType
        """
        print(f"Car is being driven by {self.driver.name}")


class CarProxy:
    """
    Car Proxy class
    """

    def __init__(self, driver: Driver):
        self.driver: Driver = driver
        self._car: Car = Car(driver)

    def drive(self) -> None:
        """
        Drive method
        :return: None
        :rtype: NoneType
        """
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print(f"{self.driver.name} is too young to drive")


if __name__ == "__main__":
    john: Driver = Driver("John", 20)
    james: Driver = Driver("James", 12)
    john_car: Car = Car(john)
    john_car.drive()
    car_proxy: CarProxy = CarProxy(james)
    car_proxy.drive()
