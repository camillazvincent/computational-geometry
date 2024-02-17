from scipy.spatial import Voronoi, voronoi_plot_2d, ConvexHull
import matplotlib.pyplot as plt
import numpy as np

def inside_convex_hull(hull, point):
    """Check if a point is inside the convex hull."""
    new_hull = ConvexHull(np.concatenate((hull.points, [point])))
    return np.array_equal(new_hull.vertices, hull.vertices)

def find_largest_circle(points):
    # Compute the convex hull of the input points
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

# Example points
points = np.array([(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)])

center, radius = find_largest_circle(points)
print(f"Center: {center}, Radius: {radius}")

vor = Voronoi(points)
fig = voronoi_plot_2d(vor)
plt.plot(points[:, 0], points[:, 1], 'o')
plt.plot(center[0], center[1], 'xr')  # Center of the largest circle
circle = plt.Circle(center, radius, color='r', fill=False)
plt.gca().add_artist(circle)
plt.show()
