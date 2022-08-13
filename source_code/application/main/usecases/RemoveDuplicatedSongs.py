from typing import List

from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.domain.main.valueobjects.DuplicatedSong import DuplicatedSong
from source_code.domain.main.valueobjects.DuplicatedSongs import DuplicatedSongs
from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs


class RemoveDuplicatedSongs:
    def __init__(self, spotify_wrapper: SpotifyWrapper):
        self.spotify_wrapper = spotify_wrapper

    def apply(self, playlist_id: str) -> None:
        songs = self.spotify_wrapper.get_songs_by(playlist_id)
        duplicated_songs = DuplicatedSongs.of(songs)
        if duplicated_songs.has_duplicates():
            self.spotify_wrapper.remove_specific_song_occurrences(playlist_id, duplicated_songs)
