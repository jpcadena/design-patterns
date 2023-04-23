"""
Classic decorator script
"""
from abc import ABC


class Shape(ABC):
    """
    Shape class that inherits from Abstract Base Class
    """

    def __str__(self):
        return ""


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    """

    def __init__(self, radius: float):
        self.radius: float = radius

    def resize(self, factor: int):
        """
        Resize the circle into a new shape
        :param factor: A factor for the shape
        :type factor: int
        :return: None
        :rtype: NoneType
        """
        self.radius *= factor

    def __str__(self):
        return f"A circle with radius {self.radius}"


class Square(Shape):
    """
    Square class that inherits from Shape
    """

    def __init__(self, side: float):
        self.side: float = side

    def __str__(self):
        return f"A square with side {self.side}"


class ColoredShape(Shape):
    """
    Colored Shape class that inherits from Shape
    """

    def __init__(self, shape: Shape, color: str):
        if isinstance(shape, ColoredShape):
            raise ValueError("Can not apply same decorator twice")
        self.shape: Shape = shape
        self.color: str = color

    def __str__(self):
        return f"{self.shape} has the color {self.color}"


class TransparentShape(Shape):
    """
    Transparent Shape class that inherits from Shape
    """

    def __init__(self, shape: Shape, transparency: float):
        self.shape: Shape = shape
        self.transparency: float = transparency

    def __str__(self):
        return f"{self.shape} has {self.transparency * 100}% transparency"


if __name__ == '__main__':
    circle: Circle = Circle(2)
    print(circle)

    red_circle: ColoredShape = ColoredShape(circle, 'red')
    print(red_circle)

    red_half_transparent_circle: TransparentShape = TransparentShape(
        red_circle, 0.5)
    print(red_half_transparent_circle)
    mixed: ColoredShape = ColoredShape(ColoredShape(Square(3), "red"), "green")
    print(mixed)

    # T(C(T(shape))
