
import utils 

def update_tracks(persons, tracks):
    """
    Met à jour les trajectoires des personnes suivies.

    Parameters
    ----------
    persons : list
        Liste des personnes détectées.
    tracks : dict
        Historique des trajectoires.
    """

    for person in persons:

        track_id = person["id"]

        if track_id is None:
            continue

        center = person["center"]

        if track_id not in tracks:
            tracks[track_id] = []

        tracks[track_id].append(center)

        # On garde seulement les 50 dernières positions
        if len(tracks[track_id]) > 50:
            tracks[track_id].pop(0)


def compute_speed(points):

    if len(points) < 2:
        return 0

    return utils.compute_distance(
        points[-1],
        points[-2]
    )