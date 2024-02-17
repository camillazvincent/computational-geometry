from scipy.spatial import Voronoi, voronoi_plot_2d, ConvexHull
import matplotlib.pyplot as plt
import numpy as np

def inside_convex_hull(hull, point):
    """
    Check if a point is inside the convex hull.

    Args:
        hull: A ConvexHull object representing the convex hull of a set of points.
        point: The point (as a numpy array) to check if it lies inside the convex hull.

    Returns:
        bool: True if the point is inside the convex hull, False otherwise.
    """
    new_hull = ConvexHull(np.concatenate((hull.points, [point])))
    return np.array_equal(new_hull.vertices, hull.vertices)

def find_largest_circle(points):
    """
    Find the center and radius of the largest circle that can fit inside the convex hull of a set of points without containing any of these points.

    Args:
        points: A numpy array of points in the format [[x1, y1], [x2, y2], ...].

    Returns:
        tuple: The coordinates of the center of the largest circle and its radius.
    """
    hull = ConvexHull(points)

    # Compute the Voronoi diagram
    vor = Voronoi(points)

    max_radius = 0
    best_vertex = None

    for vertex in vor.vertices:
        if inside_convex_hull(hull, vertex):
            # Find the minimum distance from the Voronoi vertex to all input points
            distances = np.sqrt(((points - vertex) ** 2).sum(axis=1))
            min_distance = np.min(distances)
            
            if min_distance > max_radius:
                max_radius = min_distance
                best_vertex = vertex

    return best_vertex, max_radius

# User input for points
points = np.array([tuple(map(int, point.split())) for point in input("Enter points in 'x y' format, separated by commas. For example, '0 0, 1 5, 5,1': \n").split(',')])

center, radius = find_largest_circle(points)
print(f"Center: {center}, Radius: {radius}")

vor = Voronoi(points)
fig = voronoi_plot_2d(vor)
plt.title('Largest Circle')
plt.axis('scaled')
plt.grid(True)
plt.plot(points[:, 0], points[:, 1], 'o')
plt.plot(center[0], center[1], 'xr')  # Center of the largest circle
circle = plt.Circle(center, radius, color='r')
plt.gca().add_artist(circle)
plt.show()
