from geometry import Point, LineSegment


def cross_product(vector_a, vector_b):
    """
    Calculate the cross (vector) product of two vectors.

    Args:
        vector_a (Point): The first vector.
        vector_b (Point): The second vector.

    Returns:
        float: The cross product of the two vectors.
    """
    return vector_a.x * vector_b.y - vector_a.y * vector_b.x


def subtract_points(point_a, point_b):
    """
    Subtract two points to create a vector from point2 to point1.

    Args:
        point_a (Point): The first point.
        point_b (Point): The second point.

    Returns:
        Point: The vector from point2 to point1.
    """
    return Point(point_a.x - point_b.x, point_a.y - point_b.y)


def find_intersection(line_segment1, line_segment2):
    """
    Find the intersection point of two line segments if it exists.

    Args:
        line_segment1 (LineSegment): The first line segment.
        line_segment2 (LineSegment): The second line segment.

    Returns:
        Point or None: The intersection point if the line segments intersect, otherwise None.
    """
    # Convert line endpoints to vectors
    direction_vector1 = subtract_points(line_segment1.point_2, line_segment1.point_1)
    direction_vector2 = subtract_points(line_segment2.point_2, line_segment2.point_1)

    # Calculate cross products
    cross_of_directions = cross_product(direction_vector1, direction_vector2)
    start_to_start_cross_direction1 = cross_product(subtract_points(line_segment2.point_1, line_segment1.point_1), direction_vector1)
    start_to_start_cross_direction2 = cross_product(subtract_points(line_segment2.point_1, line_segment1.point_1), direction_vector2)

    # Check for collinear and parallel cases
    if cross_of_directions == 0:
        if start_to_start_cross_direction1 == 0:
            # The line segments are collinear
            print("collinear")  # debug remove later
            return None
        else:
            # The line segments are parallel
            print("parallel")   # debug remove later
            return None

    # Calculate the intersection point
    t = start_to_start_cross_direction2 / cross_of_directions
    u = start_to_start_cross_direction1 / cross_of_directions

    # Check if the intersection point is on both line segments
    if 0 <= t <= 1 and 0 <= u <= 1:
        intersection_point = Point(line_segment1.point_1.x + t * direction_vector1.x, line_segment1.point_1.y + t * direction_vector1.y)
        return intersection_point

    # If t and u are not between 0 and 1, the line segments do not intersect
    return None


if __name__ == "__main__":
    line_segment1 = LineSegment(Point(0, 0), Point(1, 1))
    line_segment2 = LineSegment(Point(0, 1), Point(1, 0))
    line_segment3 = LineSegment(Point(0, 1), Point(1, 2))

    intersection_point = find_intersection(line_segment1, line_segment2)
    # intersection_point = find_intersection(line_segment1, line_segment3)
    print(f"Intersection at: {intersection_point.coordinates}")
