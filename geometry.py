class Point:
    """
    A representation of a single point on the coordinate plane
    """
    _counter = 0  # Class variable to keep track of the number of unnamed Point instances

    def __init__(self, x: int | float, y: int | float, name: str = None):
        self.x = x
        self.y = y
        self.coordinates = self.x, self.y
        if name is None:
            # If `name` is not provided, assign a default name based on `_counter`
            Point._counter += 1
            self.name = f"P{Point._counter}"
        else:
            self.name = name

    def __str__(self):
        return self.name


class LineSegment:
    """
    A representation of a line segment on the coordinate plane
    """
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2
        self.name = "segment " + self.point_1.name + self.point_2.name
        self.coordinates = point_1.coordinates, point_2.coordinates

    def __str__(self):
        return self.name


class Circle:
    """
    A representation of a circle on the coordinate plane
    """
    def __init__(self, center: Point, radius: int | float):
        self.center = center
        self.radius = radius
        self.name = "circle " + self.center.name
        # this naming doesn't account for concentric circles

    def __str__(self):
        return self.name


if __name__ == "__main__":
    # examples / test
    point1 = Point(0, 0)
    point2 = Point(1, 2, "Q")
    point3 = Point(1, 1, "R")
    point4 = Point(2, 2, "S")

    print(point1)
    print(point2)
    line1 = LineSegment(point1, point3)
    print(line1)
    print(line1.coordinates)

    circle1 = Circle(point1, 2)
    print(circle1)
