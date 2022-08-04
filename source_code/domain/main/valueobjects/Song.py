class Song:
    def __init__(self, name: str, spotify_id: str, release_date: str):
        self.__name = name
        self.__spotify_id = spotify_id
        self.__release_date = release_date

    def get_name(self) -> str:
        return self.__name

    def get_spotify_id(self) -> str:
        return self.__spotify_id

    def get_release_date(self) -> str:
        return self.__release_date

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Song):
            return self.__name == o.__name \
                   and self.__spotify_id == o.__spotify_id
        return False
