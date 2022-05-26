from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.domain.main.valueobjects.Playlists import Playlists


class ListUserPlaylists:
    def __init__(self, spotify_wrapper: SpotifyWrapper):
        self.spotify_wrapper = spotify_wrapper

    def apply(self) -> Playlists:
        return self.spotify_wrapper.get_user_playlists()
