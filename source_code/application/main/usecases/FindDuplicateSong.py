from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.application.main.services.FindDuplicatedSong import find_duplicated_song


class FindDuplicateSong:
    def __init__(self, spotipy: SpotifyWrapper, playlist_id: str):
        self.spotipy = spotipy
        self.playlist_id = playlist_id

    def apply(self):
        songs = self.spotipy.get_playlist_items(self.playlist_id)
        return find_duplicated_song(songs)
