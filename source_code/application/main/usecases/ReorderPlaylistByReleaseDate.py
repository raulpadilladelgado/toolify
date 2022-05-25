from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper


class ReorderPlaylistByReleaseDate:
    def __init__(self, spotipy: SpotifyWrapper, playlist_id: str):
        self.spotipy = spotipy
        self.playlist_id = playlist_id

    def apply(self):
        songs = self.spotipy.get_playlist_items(self.playlist_id)
        songs = songs.reorder_by_release_date()
        self.spotipy.replace_items(self.playlist_id, songs)
