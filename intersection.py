import matplotlib.pyplot as plt

def cross_product(ax, ay, bx, by):
    return ax * by - ay * bx

    """
    Calculate the cross product of two vectors represented by points (ax, ay) and (bx, by).

    Args:
        ax, ay: Coordinates of the first point of the first vector.
        bx, by: Coordinates of the second point of the first vector.

    Returns:
        float: The cross product of the two vectors.
    """
def subtract_points(ax, ay, bx, by):
    return ax - bx, ay - by

    """
    Subtract two points to create a vector from point B to point A.

    Args:
        ax, ay: Coordinates of point A.
        bx, by: Coordinates of point B.

    Returns:
        tuple: A vector represented by the difference between points A and B.
    """

def find_intersection(s1, s2):
    """
    Find the intersection point of two line segments if it exists.

    Args:
        s1: The first line segment represented as a tuple of its endpoints (x1, y1, x2, y2).
        s2: The second line segment represented as a tuple of its endpoints (x1, y1, x2, y2).

    Returns:
        tuple or None: The intersection point as a tuple (x, y) if the line segments intersect, otherwise None.
    """
    ax, ay, bx, by = s1
    cx, cy, dx, dy = s2
    r_px, r_py = subtract_points(bx, by, ax, ay)
    s_px, s_py = subtract_points(dx, dy, cx, cy)
    
    r_cross_s = cross_product(r_px, r_py, s_px, s_py)
    if r_cross_s == 0:
        return None  # Lines are parallel or collinear
    
    q_px, q_py = subtract_points(cx, cy, ax, ay)
    t = cross_product(q_px, q_py, s_px, s_py) / r_cross_s
    u = cross_product(q_px, q_py, r_px, r_py) / r_cross_s
    
    if 0 <= t <= 1 and 0 <= u <= 1:
        intersection_point = (ax + t * r_px, ay + t * r_py)
        print(f"Intersection at: {intersection_point}")
        return intersection_point
    
    return None

def get_lines():
    """
    Prompt the user to enter line segments and collect them.

    Returns:
        list: A list of line segments, where each line segment is represented as a tuple (x1, y1, x2, y2).
    """
    line_segments = []
    print("Enter line segments in the format 'x1 y1 x2 y2'. For example, '2 0 2 5'. Type 'E' to end.")
    while True:
        user_input = input()
        if user_input.upper() == 'E':
            break
        try:
            segment = list(map(float, user_input.split()))
            if len(segment) != 4:
                print("Invalid input.")
                continue
            line_segments.append(segment)
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
    return line_segments

line_segments = get_lines()

# Check for intersections
intersections = []
for i in range(len(line_segments)):
    for j in range(i+1, len(line_segments)):
        intersection = find_intersection(line_segments[i], line_segments[j])
        if intersection:
            intersections.append(intersection)

# Plotting
plt.figure()
for segment in line_segments:
    plt.plot([segment[0], segment[2]], [segment[1], segment[3]], marker='o')
for x, y in intersections:
    plt.plot(x, y, 'rx')  # Mark intersections with red 'x'

plt.title('Line Segment Intersections')
plt.axis('scaled')
plt.grid(True)
plt.show()