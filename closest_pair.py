import math
from geometry import Point

# References:
# https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/closepoints.pdf
# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/

class Closest_Pair:

    # Returns a tuple, first element is its distance, second element are the the points that are the closest
    def find(self, points):
    
        n = len(points)

        # find minimum distance between all nodes
        def find_min(points):

            n = len(points)
            min_dist = float('inf')
            closest_pair = None 

            for i in range(n):
                for j in range(i + 1, n):
                    d = math.dist(points[i].coordinates, points[j].coordinates)
                    if d < min_dist:
                        min_dist = d
                        closest_pair = (points[i], points[j])

            return (min_dist, closest_pair)

        # algorithm implementation
        def driver(x_sort, y_sort):

            n = len(x_sort)

            # we stop dividing when we only have 3 or less nodes
            if n <= 3:
                return find_min(x_sort)

            # divide into left and right sections and find the minimum distance between left and right sides
            mid = n // 2
            dl, left_pair = driver(x_sort[:mid], y_sort)
            dr, right_pair = driver(x_sort[mid:], y_sort)
            d = min(dl, dr)
            closest_pair = left_pair if dl < dr else right_pair

            # calculate distances between points that may have gotten stuck within the line divider
            strip = [point for point in y_sort if abs(point.x - x_sort[mid].x) < d]

            for i in range(len(strip)):
                for j in range(i + 1, len(strip)):
                    if (strip[j].y - strip[i].y) < d:
                        d = min(math.dist(strip[i].coordinates(), strip[j].coordinates()), d)
                    else:
                        break

            return d, closest_pair

        x_sorted = sorted(points, key=lambda point: point.x)
        y_sorted = sorted(points, key=lambda point: point.y)

        return driver(x_sorted, y_sorted)


# Example usage:
points = [Point(2, 3), Point(-3, 4), Point(-2.6, 3.62), Point(0.62, 5.62), Point(-1.86, 1.38), Point(-3, 1)]
pairs = Closest_Pair()
result = pairs.find(points)

print(f"First pair: {result[1][0]}")
print(f"Second pair: {result[1][1]}")
print(f"Distance between: {result[0]}")