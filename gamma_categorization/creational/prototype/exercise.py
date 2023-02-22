"""
Prototype Coding Exercise
Implement Line.deep_copy() to perform a deep copy of the given Line
 object.
This method should return a copy of a Line that contains copies of its
 start/end points.
"""


class Point:
    """
    Point class
    """

    def __init__(self, x_coordinate: int = 0, y_coordinate: int = 0):
        self.x_coordinate: int = x_coordinate
        self.y_coordinate: int = y_coordinate


class Line:
    """
    Line class
    """

    def __init__(self, start: Point = Point(), end: Point = Point()):
        self.start: Point = start
        self.end: Point = end

    def deep_copy(self):
        """
        Perform deep copy of the given Line object
        :return: Line instance
        :rtype: Line
        """
        start_copy: Point = Point(
            self.start.x_coordinate, self.start.y_coordinate)
        end_copy: Point = Point(self.end.x_coordinate, self.end.y_coordinate)
        return Line(start_copy, end_copy)


p1: Point = Point(0, 0)
p2: Point = Point(10, 10)
line1: Line = Line(p1, p2)
line2: Line = line1.deep_copy()

print("line1 start:", line1.start.x_coordinate, line1.start.y_coordinate)
print("line2 start:", line2.start.x_coordinate, line2.start.y_coordinate)

p1.x_coordinate = 5
p1.y_coordinate = 5

print("line1 start:", line1.start.x_coordinate, line1.start.y_coordinate)
print("line2 start:", line2.start.x_coordinate, line2.start.y_coordinate)
