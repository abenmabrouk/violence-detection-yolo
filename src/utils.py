import math


def get_center(bbox):
    x1, y1, x2, y2 = bbox
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    return center_x, center_y

def compute_distance(p1, p2):
    """
    Distance euclidienne entre deux points.
    """
    return math.sqrt(
        (p1[0] - p2[0])**2 +
        (p1[1] - p2[1])**2
    )

def compute_speed(points):
    """
    Calcule la vitesse en pixels/frame.
    """
    if len(points) < 2:
        return 0.0

    return compute_distance(
        points[-2],
        points[-1]
    )

def compute_direction(points):
    """
    Retourne le vecteur direction normalisé.
    """

    if len(points) < 2:
        return (0.0, 0.0)

    x1, y1 = points[-2]
    x2, y2 = points[-1]

    dx = x2 - x1
    dy = y2 - y1

    norm = math.sqrt(dx**2 + dy**2)

    if norm == 0:
        return (0.0, 0.0)

    return (
        dx / norm,
        dy / norm
    )