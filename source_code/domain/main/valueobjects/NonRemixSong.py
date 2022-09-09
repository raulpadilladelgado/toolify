class NonRemixSong:
    def __init__(self, name: str, spotify_id: str, release_date: str):
        self.__name = name
        self.__spotify_id = spotify_id
        self.__release_date = release_date

    def spotify_id(self) -> str:
        return self.__spotify_id

    def __eq__(self, o: object) -> bool:
        if isinstance(o, NonRemixSong):
            return self.__name == o.__name \
                   and self.__spotify_id == o.__spotify_id \
                   and self.__release_date == o.__release_date
        return False

    def __str__(self) -> str:
        return f'Person({self.__name},{self.spotify_id},{self.__release_date})'
