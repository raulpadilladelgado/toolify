import re
from datetime import datetime
from typing import List

from source_code.domain.main.valueobjects.Song import Song


class Songs:
    def __init__(self, songs: List[Song]):
        self.__songs = songs

    def songs(self):
        return self.__songs

    def reorder_by_release_date(self):
        return Songs(reorder(self.__songs))


def reorder(items):
    return sort(extract_release_date(items))


def extract_release_date(items):
    tracks = dict()
    for i in range(len(items)):
        if re.search("^\d{4}-\d{2}-\d{2}$", items[i]['track']['album']['release_date']):
            tracks[items[i]['track']['id']] = items[i]['track']['album']['release_date']
    return tracks


def sort(tracks):
    return list(reversed(sorted(
        tracks.items(),
        key=lambda x: datetime.strptime(x[1], "%Y-%m-%d")
    )))
