import re
from datetime import datetime


def reorder(items):
    return __sort(__extract_release_date(items))


def __extract_release_date(items):
    tracks = dict()
    for i in range(len(items)):
        if re.search("^\d{4}-\d{2}-\d{2}$", items[i]['track']['album']['release_date']):
            tracks[items[i]['track']['id']] = items[i]['track']['album']['release_date']
    return tracks


def __sort(tracks):
    return list(reversed(sorted(
        tracks.items(),
        key=lambda x: datetime.strptime(x[1], "%Y-%m-%d")
    )))
