from typing import List

from source_code.domain.main.valueobjects.Playlist import Playlist


class Playlists:
    def __init__(self, playlist_items: List[Playlist]):
        self.__playlist_items = playlist_items

    def playlist_items(self):
        return self.__playlist_items

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Playlists):
            for playlist in o.playlist_items():
                return self.__playlist_items.__contains__(playlist)
        return False

