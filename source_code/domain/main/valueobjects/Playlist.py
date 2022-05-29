class Playlist:
    def __init__(self, name: str, spotify_id: str, user_id: str, description: str, image_uri: str, total_tracks: int):
        self.__user_id: str = user_id
        self.__name: str = name
        self.__spotify_id: str = spotify_id
        self.__description: str = description
        self.__image_uri: str = image_uri
        self.__total_tracks: int = total_tracks

    def get_name(self) -> str:
        return self.__name

    def get_user_id(self) -> str:
        return self.__user_id

    def get_spotify_id(self) -> str:
        return self.__spotify_id

    def get_description(self) -> str:
        return self.__description

    def get_image_uri(self) -> str:
        return self.__image_uri

    def get_total_tracks(self) -> int:
        return self.__total_tracks

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Playlist):
            return self.__name.__eq__(o.__name) \
                   and self.__spotify_id == o.__spotify_id \
                   and self.__description == o.__description \
                   and self.__image_uri == o.__image_uri \
                   and self.__total_tracks == o.__total_tracks
        return False
