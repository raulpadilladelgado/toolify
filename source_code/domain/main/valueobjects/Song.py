from typing import List


class Song:
    def __init__(self, name: str, spotify_id: str, release_date: str, artists: List[str], album_type: str):
        self.__name = name
        self.__spotify_id = spotify_id
        self.__release_date = release_date
        self.__artists = artists
        self.__album_type = album_type

    def get_name(self) -> str:
        return self.__name

    def get_spotify_id(self) -> str:
        return self.__spotify_id

    def get_release_date(self) -> str:
        return self.__release_date

    def get_artists(self) -> List[str]:
        return self.__artists

    def get_album_type(self) -> str:
        return self.__album_type

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Song):
            return self.__name == o.__name \
                   and self.__artists == o.__artists
        return False

    def __hash__(self) -> int:
        return hash((self.__name, tuple(self.__artists)))
