from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.application.main.services.FindDuplicatedSong import find_duplicated_song
from source_code.application.main.services.GetPlaylistItems import GetPlaylistItems


class FindDuplicateSong:
    def __init__(self, spotipy: SpotifyWrapper, playlist_id: str):
        self.get_playlist_items = GetPlaylistItems(spotipy, playlist_id)

    def apply(self):
        songs = self.get_playlist_items.apply()
        return find_duplicated_song(songs)
