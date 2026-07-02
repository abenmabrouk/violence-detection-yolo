import config


def compute_behavior(person):
    """
    Compute behavior descriptors for one tracked person.

    Parameters
    ----------
    person : dict

    Returns
    -------
    dict
    """

    motion = person.get("motion", {})

    speed = motion.get("speed", 0.0)
    acceleration = motion.get("acceleration", 0.0)
    distance = motion.get("distance_traveled", 0.0)

    density = person.get("density", 0)

    behavior = {
        "running": detect_running(speed),
        "high_acceleration": detect_high_acceleration(acceleration),
        "high_density": detect_high_density(density),
        "risk_score": 0,
        "risk_level": "NORMAL"
    }

    score = compute_risk_score(
        speed=speed,
        acceleration=acceleration,
        density=density
    )

    behavior["risk_score"] = score
    behavior["risk_level"] = classify_behavior(score)

    return behavior


def detect_running(speed):
    """
    Detect running behavior.
    """

    return speed >= config.RUNNING_SPEED_THRESHOLD


def detect_high_acceleration(acceleration):
    """
    Detect sudden acceleration.
    """

    return acceleration >= config.ACCELERATION_THRESHOLD


def detect_high_density(density):
    """
    Detect crowded situations.
    """

    return density >= config.DENSITY_THRESHOLD


def compute_risk_score(speed, acceleration, density):
    """
    Compute a simple rule-based risk score.
    """

    score = 0

    if speed >= config.RUNNING_SPEED_THRESHOLD:
        score += 2

    if acceleration >= config.ACCELERATION_THRESHOLD:
        score += 2

    if density >= config.DENSITY_THRESHOLD:
        score += 1

    return score


def classify_behavior(score):
    """
    Convert score into a behavior label.
    """

    if score >= 5:
        return "HIGH"

    if score >= 3:
        return "MEDIUM"

    return "NORMAL"