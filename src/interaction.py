import math
import config

def compute_distance(center1, center2):
    """
    Compute Euclidean distance between two centers.

    Parameters
    ----------
    center1 : tuple
    center2 : tuple

    Returns
    -------
    float
    """

    dx = center1[0] - center2[0]
    dy = center1[1] - center2[1]

    return math.sqrt(dx ** 2 + dy ** 2)

def compute_pairwise_distances(persons):
    """
    Compute distances between every pair of persons.

    Returns
    -------
    list
    """

    interactions = []

    n = len(persons)

    for i in range(n):

        for j in range(i + 1, n):

            person1 = persons[i]
            person2 = persons[j]

            distance = compute_distance(
                person1["center"],
                person2["center"]
            )

            interactions.append({

                "person1": person1["id"],

                "person2": person2["id"],

                "distance": distance

            })

    return interactions

def find_nearest_neighbors(persons):
    """
    Find nearest neighbor for each person.

    Returns
    -------
    dict
    """

    neighbors = {}

    for person in persons:

        best_distance = float("inf")
        best_neighbor = None

        for other in persons:

            if person["id"] == other["id"]:
                continue

            distance = compute_distance(
                person["center"],
                other["center"]
            )

            if distance < best_distance:

                best_distance = distance
                best_neighbor = other["id"]

        neighbors[person["id"]] = {

            "neighbor": best_neighbor,

            "distance": best_distance

        }

    return neighbors


def detect_close_contacts(interactions):
    """
    Return close interactions.
    """

    contacts = []

    for interaction in interactions:

        if interaction["distance"] < config.INTERACTION_DISTANCE:

            contacts.append(interaction)

    return contacts

def compute_local_density(persons, radius):
    """
    Count neighbors around each person.
    """

    density = {}

    for person in persons:

        count = 0

        for other in persons:

            if person["id"] == other["id"]:
                continue

            distance = compute_distance(
                person["center"],
                other["center"]
            )

            if distance < radius:
                count += 1

        density[person["id"]] = count

    return density