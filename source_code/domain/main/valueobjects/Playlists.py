from typing import List

from source_code.domain.main.valueobjects.Playlist import Playlist


class Playlists:
    def __init__(self, playlist_items: List[Playlist]):
        self.__playlist_items: List[Playlist] = playlist_items

    def playlist_items(self) -> List[Playlist]:
        return self.__playlist_items

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Playlists) and len(o.__playlist_items) == len(self.__playlist_items):
            return o.__playlist_items == self.__playlist_items
        return False
