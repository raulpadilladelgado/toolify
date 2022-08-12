from typing import List

from source_code.domain.main.valueobjects.DuplicatedSong import DuplicatedSong


class DuplicatedSongs:
    def __init__(self, songs: List[DuplicatedSong]):
        self.__songs = songs

    def __eq__(self, o: object) -> bool:
        if isinstance(o, DuplicatedSongs) and len(o.__songs) == len(self.__songs):
            return o.__songs == self.__songs
        return False
