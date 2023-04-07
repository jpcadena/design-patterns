"""
Decorator Coding Exercise
"""


class Circle:
    """
    Circle class.
    """

    def __init__(self, radius: float):
        self.radius: float = radius

    def resize(self, factor: int):
        """
        Resize the circle
        :param factor: The factor to resize the circle
        :type factor:
        :return: None
        :rtype: NoneType
        """
        self.radius *= factor

    def __str__(self):
        return f"A circle of radius {self.radius}"


class Square:
    """
    Square class
    """

    def __init__(self, side: float):
        self.side: float = side

    def __str__(self):
        return f"A square with side {self.side}"


class ColoredShape:
    """
    Colored Shape class
    """

    def __init__(self, shape, color: str):
        self.color: str = color
        self.shape = shape

    def resize(self, factor: int):
        """
        Resize the colored shape
        :param factor: The factor to resize the colored shape
        :type factor: int
        :return: None
        :rtype: NoneType
        """
        if hasattr(self.shape, 'resize'):
            self.shape.resize(factor)

    def __str__(self):
        return f"{self.shape} has the color {self.color}"
