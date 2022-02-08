from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.application.main.services.TransformItemToPlaylist import transform_items_to_playlists


class ListUserPlaylists:
    def __init__(self, spotipy: SpotifyWrapper):
        self.spotipy = spotipy

    def apply(self):
        playlists = self.spotipy.get_playlists()
        user_id = self.spotipy.get_user()
        return transform_items_to_playlists(playlists, user_id)
