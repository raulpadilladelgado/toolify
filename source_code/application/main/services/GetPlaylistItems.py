import string

from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper


class GetPlaylistItems:
    def __init__(self, spotipy: SpotifyWrapper, playlist_id: string):
        self.spoti_wrapper = spotipy
        self.playlist_id = playlist_id

    def apply(self):
        items = self.spoti_wrapper.get_playlist_items(self.playlist_id)
        return items
