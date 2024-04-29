"""
Geometric shape script for Composite design pattern
"""

from typing import Any, Optional


class GraphicObject:
    """
    Graphic object class.
    """

    def __init__(self, color: Optional[str] = None, name: str = "Group"):
        self.color: Optional[str] = color
        self.children: list[Any] = []
        self._name: str = name

    @property
    def name(self) -> str:
        """
        Property for the attribute name of the Graphic object
        """
        return self._name

    def str_helper(self, depth: int) -> str:
        """
        String helper function
        :param depth: The depth of the graphic object
        :type depth: int
        :return: Object string representation
        :rtype: str
        """
        items: list[str] = ["*" * depth]
        if self.color:
            items.append(self.color)
        items.append(f"{self.name}\n")
        for child in self.children:
            items.append(child.str_helper(depth + 1))
        return "".join(items)

    def __str__(self) -> str:
        return self.str_helper(0)


class Circle(GraphicObject):
    """
    Circle class that inherits from GraphicObject.
    """

    @property
    def name(self) -> str:
        return "Circle"


class Square(GraphicObject):
    """
    Square class that inherits from GraphicObject.
    """

    @property
    def name(self) -> str:
        return "Square"


if __name__ == "__main__":
    drawing: GraphicObject = GraphicObject(name="My drawing")
    drawing.children.append(Circle("Red"))
    drawing.children.append(Square("Green"))

    group: GraphicObject = GraphicObject()
    group.children.append(Circle("Blue"))
    group.children.append(Square("Yellow"))
    drawing.children.append(group)

    print(str(drawing))
