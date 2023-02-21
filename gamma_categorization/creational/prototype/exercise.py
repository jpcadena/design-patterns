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

    def __init__(self, x: int = 0, y: int = 0):
        self.x: int = x
        self.y: int = y


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
        start_copy: Point = Point(self.start.x, self.start.y)
        end_copy: Point = Point(self.end.x, self.end.y)
        return Line(start_copy, end_copy)


p1: Point = Point(0, 0)
p2: Point = Point(10, 10)
line1: Line = Line(p1, p2)
line2: Line = line1.deep_copy()

print("line1 start:", line1.start.x, line1.start.y)
print("line2 start:", line2.start.x, line2.start.y)

p1.x = 5
p1.y = 5

print("line1 start:", line1.start.x, line1.start.y)
print("line2 start:", line2.start.x, line2.start.y)
