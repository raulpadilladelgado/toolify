class Song:
    def __init__(self, name: str, spotify_id: str):
        self.__name = name
        self.__spotify_id = spotify_id

    def get_name(self):
        return self.__name

    def get_spotify_id(self):
        return self.__spotify_id
