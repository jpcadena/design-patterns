"""
Adapter with no caching script
"""

# A construct which adapts an existing interface to conform to the required
# interface


class Point:
    """
    Point class
    """

    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate: int = x_coordinate
        self.y_coordinate: int = y_coordinate

    @staticmethod
    def draw_point() -> None:
        """
        Draws a point
        :return: None
        :rtype: NoneType
        """
        print(".", end=" ")


class Line:
    """
    Line class
    """

    def __init__(self, start: Point, end: Point):
        self.start: Point = start
        self.end: Point = end


class Rectangle(list[Line]):
    """
    Rectangle class
    """

    def __init__(
        self, x_coordinate: int, y_coordinate: int, width: int, height: int
    ):
        super().__init__()
        self.append(
            Line(
                Point(x_coordinate, y_coordinate),
                Point(x_coordinate + width, y_coordinate),
            )
        )
        self.append(
            Line(
                Point(x_coordinate + width, y_coordinate),
                Point(x_coordinate + width, y_coordinate + height),
            )
        )
        self.append(
            Line(
                Point(x_coordinate, y_coordinate),
                Point(x_coordinate, y_coordinate + height),
            )
        )
        self.append(
            Line(
                Point(x_coordinate, y_coordinate + height),
                Point(x_coordinate + width, y_coordinate + height),
            )
        )


class LineToPointAdapter(list[Point]):
    """
    Adapter for Line to Point class
    """

    instance_count: int = 0

    def __init__(self, line: Line):
        super().__init__()
        self.instance_count += 1
        print(
            f"{self.instance_count}: Generating points for line ["
            f"{line.start.x_coordinate},{line.start.y_coordinate}] -> ["
            f"{line.end.x_coordinate},{line.end.y_coordinate}]"
        )
        left = min(line.start.x_coordinate, line.end.x_coordinate)
        right = max(line.start.x_coordinate, line.end.x_coordinate)
        top = min(line.start.y_coordinate, line.end.y_coordinate)
        bottom = min(line.start.y_coordinate, line.end.y_coordinate)
        if right - left == 0:
            for y_value in range(top, bottom):
                self.append(Point(left, y_value))
        elif line.end.y_coordinate - line.start.y_coordinate == 0:
            for x_value in range(left, right):
                self.append(Point(x_value, top))


def draw(rectangles: list[Rectangle]) -> None:
    """
    Draws multiple rectangles
    :param rectangles: List of rectangles to draw
    :type rectangles: list[Rectangle]
    :return: None
    :rtype: NoneType
    """
    print("\n\n--- Drawing some stuff ---\n")
    for rectangle in rectangles:
        for line in rectangle:
            adapter: LineToPointAdapter = LineToPointAdapter(line)
            for point in adapter:
                point.draw_point()


if __name__ == "__main__":
    rectangles_list: list[Rectangle] = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6),
    ]
    draw(rectangles_list)
