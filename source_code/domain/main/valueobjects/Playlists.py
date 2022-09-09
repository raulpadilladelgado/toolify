from typing import List

from source_code.domain.main.valueobjects.Playlist import Playlist


class Playlists:
    def __init__(self, playlists: List[Playlist]):
        self.__values: List[Playlist] = playlists

    def values(self) -> List[Playlist]:
        return self.__values

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Playlists) and len(o.__values) == len(self.__values):
            return o.__values == self.__values
        return False
