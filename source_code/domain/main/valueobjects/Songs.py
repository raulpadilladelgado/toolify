from __future__ import annotations

from typing import List

from source_code.domain.main.exceptions.SongsCreationError import SongsCreationError
from source_code.domain.main.valueobjects.Song import Song


class Songs(object):
    __create_key = object()

    @classmethod
    def create(cls, songs: List[Song]) -> Songs:
        if len(songs) == 0:
            raise SongsCreationError("At least one song is needed to build songs")
        return Songs(cls.__create_key, songs)

    def __init__(self, create_key: object, songs: List[Song]) -> None:
        assert (create_key == Songs.__create_key), \
            "Songs objects must be created using Songs.create"
        self.__songs = songs

    def songs(self) -> List[Song]:
        return self.__songs

    def songs_ids(self) -> List[str]:
        return list(map(lambda song: song.get_spotify_id(), self.__songs))

    def reorder_by_release_date(self) -> 'Songs':
        self.__songs.sort(
            key=lambda x: x.get_release_date(), reverse=True
        )
        return Songs.create(self.__songs)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Songs) and len(o.__songs) == len(self.__songs):
            return o.__songs == self.__songs
        return False
