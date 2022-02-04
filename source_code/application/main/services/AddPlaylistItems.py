import array
import string

from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper


class AddPlaylistItems:
    def __init__(self, spotipy: SpotifyWrapper, playlist_id: string, songs_ids: array):
        self.spoti_wrapper = spotipy
        self.playlist_id = playlist_id
        self.songs_ids = songs_ids

    def apply(self):
        self.spoti_wrapper.playlist_add_items(self.playlist_id, self.songs_ids)
