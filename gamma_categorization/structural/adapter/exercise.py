"""
Adapter Coding Exercise
"""


class Square:
    """
    Square class
    """

    def __init__(self, side: int = 0):
        self.side: int = side


class SquareToRectangleAdapter:
    """
    Square to Rectangle Adapter class
    """

    def __init__(self, square: Square):
        self.square: Square = square

    @property
    def width(self):
        """
        Width of the square
        :return: The width of the square
        :rtype: int
        """
        return self.square.side

    @property
    def height(self):
        """
        Height of the square
        :return: The height of the square
        :rtype: int
        """
        return self.square.side


def calculate_area(rectangle: SquareToRectangleAdapter) -> int:
    """
    Calculate area of rectangle
    :param rectangle:
    :type rectangle:
    :return:
    :rtype:
    """
    return rectangle.width * rectangle.height


my_square: Square = Square(11)
adapter: SquareToRectangleAdapter = SquareToRectangleAdapter(my_square)
area: int = calculate_area(adapter)
print(area)

my_square.side = 10
area = calculate_area(adapter)
print(area)
