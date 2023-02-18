"""
Liskov Substitution Principle
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width: int, height: int) -> None:
        self._height: int = height
        self._width: int = width

    @property
    def area(self) -> int:
        """
        Property to calculate area
        :return: width times height
        :rtype:int
        """
        return self._width * self._height

    def __str__(self) -> str:
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self) -> int:
        """
        Width getter property
        :return: width
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        """
        Width property setter
        :param value: new width
        :type value: int
        :return: None
        :rtype: NoneType
        """
        self._width: int = value

    @property
    def height(self) -> int:
        """
        Height getter property
        :return: height
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        """
        Height setter property
        :param value: new height
        :type value: int
        :return: None
        :rtype: NoneType
        """
        self._height: int = value


class Square(Rectangle):
    """
    Square class inherits from Rectangle
    """
    def __init__(self, size: int) -> None:
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value: int) -> None:
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value: int) -> None:
        _width = _height = value


def use_it(rectangle: Rectangle) -> None:
    """
    Use method for rectangle object
    :param rectangle: object
    :type rectangle:Rectangle
    :return: None
    :rtype: NoneType
    """
    width: int = rectangle.width
    rectangle.height = 10  # unpleasant side effect
    expected: int = width * 10
    print(f'Expected an area of {expected}, got {rectangle.area}')


my_rectangle: Rectangle = Rectangle(2, 3)
use_it(my_rectangle)

square: Square = Square(5)
use_it(square)
