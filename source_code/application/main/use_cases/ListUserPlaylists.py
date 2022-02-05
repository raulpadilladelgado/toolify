from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.application.main.services.GetPlaylists import GetPlaylists
from source_code.application.main.services.GetUserId import GetUserId
from source_code.application.main.services.TransformItemToPlaylist import transform_items_to_playlists


class ListUserPlaylists:
    def __init__(self, spotipy: SpotifyWrapper):
        self.spotipy = spotipy
        self.get_playlists = GetPlaylists(spotipy)
        self.get_user_id = GetUserId(spotipy)

    def apply(self):
        results = self.get_playlists.apply()
        user_id = self.get_user_id.apply()
        return transform_items_to_playlists(results, user_id)
