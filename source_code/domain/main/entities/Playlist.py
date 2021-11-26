class Playlist:
    def __init__(self, name, spotify_id, description, image_uri, total_tracks):
        self.__name = name
        self.__spotify_id = spotify_id
        self.__description = description
        self.__image_uri = image_uri
        self.__total_tracks = total_tracks

    def get_name(self):
        return self.__name

    def get_spotify_id(self):
        return self.__spotify_id

    def get_description(self):
        return self.__description

    def get_image_uri(self):
        return self.__image_uri

    def get_total_tracks(self):
        return self.__total_tracks




