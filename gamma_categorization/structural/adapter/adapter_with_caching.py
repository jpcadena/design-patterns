"""
Adapter with caching script
"""
from gamma_categorization.structural.adapter.adapter import draw, Point, \
    Line, Rectangle


class LineToPointAdapter(list[Point]):
    """
    Adapter for Line to Point class
    """
    cache: dict[int, list[Point]] = {}

    def __init__(self, line: Line):
        self.hash = hash(line)
        if self.hash in self.cache:
            return
        super().__init__()
        print(f"Generating points for line "
              f"[{line.start.x_coordinate},{line.start.y_coordinate}] ->"
              f" [{line.end.x_coordinate},{line.end.y_coordinate}]")
        left = min(line.start.x_coordinate, line.end.x_coordinate)
        right = max(line.start.x_coordinate, line.end.x_coordinate)
        top = min(line.start.y_coordinate, line.end.y_coordinate)
        bottom = min(line.start.y_coordinate, line.end.y_coordinate)
        points: list[Point] = []
        if right - left == 0:
            for y_value in range(top, bottom):
                points.append(Point(left, y_value))
        elif line.end.y_coordinate - line.start.y_coordinate == 0:
            for x_value in range(left, right):
                points.append(Point(x_value, top))
        self.cache[self.hash] = points

    def __iter__(self):
        return iter(self.cache[self.hash])


if __name__ == '__main__':
    rectangles_list: list[Rectangle] = [
        Rectangle(1, 1, 10, 10), Rectangle(3, 3, 6, 6)]
    draw(rectangles_list)
