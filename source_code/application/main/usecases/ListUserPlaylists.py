from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.domain.main.valueobjects.Playlists import Playlists


class ListUserPlaylists:
    def __init__(self, spotipy: SpotifyWrapper):
        self.spotipy = spotipy

    def apply(self) -> Playlists:
        return self.spotipy.get_user_playlists()
