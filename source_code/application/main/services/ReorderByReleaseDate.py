import re
from collections import OrderedDict
from datetime import datetime


def reorder(items):
    tracks = dict()
    for i in range(len(items)):
        if re.search("^\d{4}-\d{2}-\d{2}$", items[i]['track']['album']['release_date']):
            tracks[items[i]['track']['id']] = items[i]['track']['album']['release_date']
    reordered_songs = OrderedDict(reversed(sorted(
        tracks.items(),
        key=lambda x: datetime.strptime(x[1], "%Y-%m-%d")
    )))
    return list(reordered_songs.keys())
