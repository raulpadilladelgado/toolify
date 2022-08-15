from typing import List


class DuplicatedSong:
    def __init__(self, name: str, spotify_id: str, release_date: str, positions: List[int]):
        self.__name = name
        self.__spotify_id = spotify_id
        self.__release_date = release_date
        self.__positions = positions

    def spotify_id(self) -> str:
        return self.__spotify_id

    def positions(self) -> List[int]:
        return self.__positions

    def __eq__(self, o: object) -> bool:
        if isinstance(o, DuplicatedSong):
            return self.__name == o.__name \
                   and self.__spotify_id == o.__spotify_id \
                   and self.__release_date == o.__release_date \
                   and self.__positions == o.__positions
        return False
