import array
import string

from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper


class AddPlaylistItems:
    def __init__(self, spotipy: SpotifyWrapper, playlist_id: string):
        self.spoti_wrapper = spotipy
        self.playlist_id = playlist_id

    def apply(self, songs_ids: array):
        self.spoti_wrapper.playlist_add_items(self.playlist_id, songs_ids)
