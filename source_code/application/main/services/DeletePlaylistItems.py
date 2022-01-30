import string

from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper


class DeletePlaylistItems:
    def __init__(self, spotipy: SpotifyWrapper, playlist_id: string):
        self.spoti_wrapper = spotipy
        self.playlist_id = playlist_id

    def apply(self):
        self.spoti_wrapper.delete_all_items(self.playlist_id)
