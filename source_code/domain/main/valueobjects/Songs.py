from typing import List

from source_code.domain.main.valueobjects.Song import Song


class Songs:
    def __init__(self, songs: List[Song]):
        self.__songs = songs

    def songs(self) -> List[Song]:
        return self.__songs

    def songs_ids(self) -> List[str]:
        return list(map(lambda song: song.get_spotify_id(), self.__songs))

    def reorder_by_release_date(self):
        self.__songs.sort(
            key=lambda x: x.get_release_date(), reverse=True
        )
        return Songs(self.__songs)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Songs) and len(o.__songs) == len(self.__songs):
            return o.__songs == self.__songs
        return False
