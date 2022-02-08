from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.application.main.services.ReorderByReleaseDate import reorder


class ReorderPlaylist:
    def __init__(self, spotipy: SpotifyWrapper, playlist_id: str):
        self.spotipy = spotipy
        self.playlist_id = playlist_id

    def apply(self):
        songs = self.spotipy.get_playlist_items(self.playlist_id)
        reordered_songs = reorder(songs)
        self.spotipy.delete_all_items(self.playlist_id)
        self.spotipy.playlist_add_items(self.playlist_id, reordered_songs)
