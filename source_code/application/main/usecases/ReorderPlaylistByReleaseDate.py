from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.domain.main.valueobjects.Songs import Songs


class ReorderPlaylistByReleaseDate:
    def __init__(self, spotipy: SpotifyWrapper, playlist_id: str):
        self.spotipy = spotipy
        self.playlist_id = playlist_id

    def apply(self) -> None:
        songs: Songs = self.spotipy.get_songs_by(self.playlist_id).reorder_by_release_date()
        self.spotipy.replace_songs_by(self.playlist_id, songs)
