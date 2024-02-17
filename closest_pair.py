import math
from geometry import Point

# References:
# https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/closepoints.pdf
# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/

def brute_force_pair(points):

    """
        Function to find the distance between a given set of points using least optimal solution.

        Args:
            points: a set of points

        Returns a tuple:
            - First element: Distance
            - Second element: Closest points
    """

    n = len(points)
    min_dist = float('inf')
    closest_pair = None 

    # check every possible pair of points for the minimum distance
    for i in range(n):
        for j in range(i + 1, n):
            d = math.dist(points[i].coordinates, points[j].coordinates)
            if d < min_dist:
                min_dist = d
                closest_pair = (points[i], points[j])

    return (min_dist, closest_pair)

def optimized_pair(x_sort, y_sort):

    """
        Function to find the distance between a given set of points using optimal solution.

        Args:
            x_sort: sorted set of points by ascending x values
            y_sort: sorted set of points by ascending y values

        Returns a tuple:
            - First element: Distance
            - Second element: Closest points
    """

    n = len(x_sort)

    # we stop dividing when we only have 3 or less nodes
    if n <= 3:
        return brute_force_pair(x_sort)

    # divide into left and right sections and find the minimum distance between left and right sides
    mid = n // 2
    dl, left_pair = optimized_pair(x_sort[:mid], y_sort)
    dr, right_pair = optimized_pair(x_sort[mid:], y_sort)
    d = min(dl, dr)
    closest_pair = left_pair if dl < dr else right_pair

    # calculate distances between points that may have gotten stuck within the line divider
    strip = [point for point in y_sort if abs(point.x - x_sort[mid].x) < d]

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j].y - strip[i].y) < d:
                d = min(math.dist(strip[i].coordinates, strip[j].coordinates), d)
            else:
                break

    return d, closest_pair


def closest_pair(points):

    """
        Function to sort points and run the optimal solution.

        Args:
            points: a set of points

        Returns a tuple:
            - First element: Distance
            - Second element: Closest points
    """
    
    x_sorted = sorted(points, key=lambda point: point.x)
    y_sorted = sorted(points, key=lambda point: point.y)

    return optimized_pair(x_sorted, y_sorted)