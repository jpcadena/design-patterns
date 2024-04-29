"""
Bridge script
"""

from abc import ABC


class Renderer(ABC):
    """
    Renderer class that inherits from Abstract Base Class.
    """

    def render_circle(self, radius: float) -> None:
        """
        Render a circle
        :param radius: Radius of the circle
        :type radius: float
        :return: None
        :rtype: NoneType
        """


class VectorRenderer(Renderer):
    """
    Vector Renderer class that inherits from Renderer.
    """

    def render_circle(self, radius: float) -> None:
        print(f"Drawing a circle of radius {radius}")


class RasterRenderer(Renderer):
    """
    Raster Renderer class that inherits from Renderer.
    """

    def render_circle(self, radius: float) -> None:
        print(f"Drawing pixels for a circle of radius {radius}")


class Shape:
    """
    Shape class
    """

    def __init__(self, renderer: Renderer):
        self.renderer: Renderer = renderer

    def draw(self) -> None:
        """
        Draw the shape
        :return: None
        :rtype: NoneType
        """

    def resize(self, factor: int) -> None:
        """
        Resize the shape
        :param factor: Factor to use for the shape
        :type factor: int
        :return: None
        :rtype: NoneType
        """


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    """

    def __init__(self, renderer: Renderer, radius: float):
        super().__init__(renderer)
        self.radius: float = radius

    def draw(self) -> None:
        self.renderer.render_circle(self.radius)

    def resize(self, factor: int) -> None:
        self.radius *= factor


if __name__ == "__main__":
    raster_renderer: RasterRenderer = RasterRenderer()
    vector_renderer: VectorRenderer = VectorRenderer()
    circle: Circle = Circle(vector_renderer, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
