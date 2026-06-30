import math


def compute_speed(previous_center, current_center, fps):
    """
    Compute speed in pixels/second.

    Parameters
    ----------
    previous_center : tuple
        (x, y) of previous frame.

    current_center : tuple
        (x, y) of current frame.

    fps : float

    Returns
    -------
    float
    """

    dx = current_center[0] - previous_center[0]
    dy = current_center[1] - previous_center[1]

    distance = math.sqrt(dx**2 + dy**2)

    speed = distance * fps

    return speed


def compute_direction(previous_center, current_center):
    """
    Compute normalized motion vector.

    Returns
    -------
    tuple
        (dx, dy)
    """

    dx = current_center[0] - previous_center[0]
    dy = current_center[1] - previous_center[1]

    norm = math.sqrt(dx**2 + dy**2)

    if norm == 0:
        return (0.0, 0.0)

    return (
        dx / norm,
        dy / norm
    )


def compute_angle(direction):
    """
    Compute motion angle in degrees.

    Returns
    -------
    float
    """

    dx, dy = direction

    angle = math.degrees(math.atan2(dy, dx))

    return angle


def compute_acceleration(previous_speed, current_speed, fps):
    """
    Compute acceleration in pixels/s².
    """

    dt = 1.0 / fps

    acceleration = (current_speed - previous_speed) / dt

    return acceleration


def compute_distance_traveled(track):
    """
    Compute cumulative travelled distance.

    Parameters
    ----------
    track : list
        List of centers.

    Returns
    -------
    float
    """

    if len(track) < 2:
        return 0.0

    distance = 0.0

    for i in range(1, len(track)):

        x1, y1 = track[i - 1]
        x2, y2 = track[i]

        distance += math.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        )

    return distance


def compute_motion(track, fps):
    """
    Compute all motion descriptors.

    Parameters
    ----------
    track : list
        List of tracked centers.

    fps : float

    Returns
    -------
    dict
    """

    if len(track) < 2:

        return {
            "speed": 0.0,
            "direction": (0.0, 0.0),
            "angle": 0.0,
            "acceleration": 0.0,
            "distance": 0.0
        }

    previous = track[-2]
    current = track[-1]

    speed = compute_speed(
        previous,
        current,
        fps
    )

    direction = compute_direction(
        previous,
        current
    )

    angle = compute_angle(direction)

    distance = compute_distance_traveled(track)

    acceleration = 0.0

    if len(track) >= 3:

        old_speed = compute_speed(
            track[-3],
            track[-2],
            fps
        )

        acceleration = compute_acceleration(
            old_speed,
            speed,
            fps
        )

    return {

        "speed": speed,

        "direction": direction,

        "angle": angle,

        "acceleration": acceleration,

        "distance": distance

    }