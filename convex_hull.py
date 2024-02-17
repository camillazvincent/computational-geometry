import matplotlib.pyplot as plt
import numpy as np


def orientation(p, q, r):
    """
    Function to find orientation of ordered triplet (p, q, r).
    Returns:
     - 0: Collinear
     - 1: Clockwise
     - 2: Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or Counterclockwise


def convex_hull(points):
    """
    Function to compute the convex hull of a set of points using the Gift Wrapping Algorithm (Jarvis March).
    """
    n = len(points)
    if n < 3:
        return print("Convex hull not possible")

    # Initialize result list
    hull = []

    # Find the leftmost point
    left = min(range(n), key=lambda x: points[x][0])
    point = left
    q = 0

    while True:
        hull.append(point)

        # Search for a point 'q' such that orientation(point, q, r) is counterclockwise
        q = (point + 1) % n
        for r in range(n):
            if orientation(points[point], points[q], points[r]) == 2:
                q = r

        point = q

        # If we looped back to the starting point, the hull is complete
        if point == left:
            break

    # Output result
    return [points[i] for i in hull]

def plot_convex_hull(points, hull_points):
    plt.figure()
    xs, ys = zip(*points)  # Unpack the points
    plt.scatter(xs, ys)  # Plot the points

    hull_xs, hull_ys = zip(*hull_points + [hull_points[0]])  # Ensure the hull is closed by repeating the first point
    plt.plot(hull_xs, hull_ys, 'r-')  # Plot the convex hull

    plt.title('Convex Hull')
    plt.axis('scaled')
    plt.grid(True)
    plt.show()


def main():
    points = np.array([tuple(map(int, point.split())) for point in input("Enter points in 'x y' format, separated by commas. For example, '0 0, 1 5, 5,1': \n").split(',')])
    hull_points = convex_hull(points)
    hull_points_tuples = [tuple(point) for point in hull_points]
    print(hull_points_tuples)
    print("This is considered a Convex Hull from the given points")
    plot_convex_hull(points, hull_points)



if __name__ == "__main__":
    main()
