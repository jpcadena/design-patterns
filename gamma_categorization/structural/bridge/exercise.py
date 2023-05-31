"""
Bridge Coding Exercise
"""
from abc import ABC
from typing import Any, Optional


class Renderer(ABC):
    """
    Renderer class
    """

    @property
    def what_to_render_as(self) -> Any:
        """
        What to render as
        :return: None
        :rtype: NoneType
        """
        return None


class VectorRenderer(Renderer):
    """
    Vector renderer class
    """

    @property
    def what_to_render_as(self) -> str:
        return "lines"


class RasterRenderer(Renderer):
    """
    Raster renderer class
    """

    @property
    def what_to_render_as(self) -> str:
        return "pixels"


class Shape(ABC):
    """
    Shape class that inherits from Abstract Base Class
    """

    def __init__(self, renderer: Renderer):
        self.renderer: Renderer = renderer
        self.name: Optional[str] = None

    def __str__(self) -> str:
        return f"Drawing {self.name} as {self.renderer.what_to_render_as}"


class Triangle(Shape):
    """
    Triangle class that inherits from Shape
    """

    def __init__(self, renderer: Renderer):
        super().__init__(renderer)
        self.name = "Triangle"


class Square(Shape):
    """
    Square class that inherits from Shape
    """

    def __init__(self, renderer: Renderer):
        super().__init__(renderer)
        self.name: str = "Square"


# Usage example
triangle: Triangle = Triangle(RasterRenderer())
print(str(triangle))
