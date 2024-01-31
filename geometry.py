class Point:
    """
    A representation of a single point on the coordinate plane


    """
    def __init__(self, x: int | float, y: int | float, name: str = None):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return f"{self.name if self.name else ''}({self.x}, {self.y})"

    def coordinates(self):
        return self.x, self.y


class Line:
    """
    A representation of a line segment on the coordinate plane


    """
    def __init__(self, *points):
        # Test if all points form a single line
        self.points = points
        if len(points) < 2:
            raise ValueError("Must provide at least 2 points")
        for i in range(len(points) - 2):
            p1, p2, p3 = points[i], points[i + 1], points[i + 2]

            # Calculate area of triangle formed by p1, p2, p3
            area = 0.5 * abs(p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y))

            if area != 0:
                raise ValueError("Points are not collinear")

    def __str__(self):
        rep = ''
        for i in range(len(self.points)):
            rep += f"{self.points[i].name}"
            # Overline character: \u0304

        return rep


# examples / test
point1 = Point(0, 0, "P")
point2 = Point(1, 2, "Q")
point3 = Point(1, 1, "R")
point4 = Point(2, 2, "S")

print(point1)
print(point2)
line1 = Line(point1, point3, point4)
print(line1)
