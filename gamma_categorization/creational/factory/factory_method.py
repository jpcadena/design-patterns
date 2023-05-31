"""
Factory method script
"""
from math import cos, sin
from typing import Any


class Point:
    """
    Point class
    """

    def __init__(self, x_coordinate: float, y_coordinate: float):
        self.x_coordinate: float = x_coordinate
        self.y_coordinate: float = y_coordinate

    def __str__(self) -> str:
        return f"x: {self.x_coordinate}, y: {self.y_coordinate}"

    @staticmethod
    def new_cartesian_point(x_coordinate: float, y_coordinate: float) -> Any:
        """
        Factory initializer method for Cartesian Point
        :param x_coordinate: X-coordinate of the point
        :type x_coordinate: float
        :param y_coordinate: Y-coordinate of the point
        :type y_coordinate: float
        :return: Point instance
        :rtype: Point
        """
        return Point(x_coordinate, y_coordinate)

    @staticmethod
    def new_polar_point(rho: float, theta: float) -> Any:
        """
        Factory initializer method for Polar Point
        :param rho: Distance of the vector
        :type rho: float
        :param theta: Angle
        :type theta: float
        :return: Point instance
        :rtype: Point
        """
        return Point(rho * cos(theta), rho * sin(theta))


point: Point = Point(2, 3)
point2: Point = Point.new_polar_point(1, 2)
print(point)
print(point2)
