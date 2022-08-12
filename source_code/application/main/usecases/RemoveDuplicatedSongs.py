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
        duplicated_songs = find_duplicated_songs(songs)
        if not duplicated_songs:
            return
        self.spotify_wrapper.remove_specific_song_occurrences(playlist_id, duplicated_songs)


def find_duplicated_songs(songs: Songs) -> DuplicatedSongs:
    duplicated_songs = []
    unique_songs = filter_unique_songs(songs.songs())
    for unique_song in unique_songs:
        indexes = [index for index, song in enumerate(songs.songs()) if song == unique_song]
        if len(indexes) > 1:
            indexes.pop(0)
            duplicated_songs.append(
                DuplicatedSong(unique_song.get_name(), unique_song.get_spotify_id(), unique_song.get_release_date(),
                               indexes)
            )
    return DuplicatedSongs(duplicated_songs)


def filter_unique_songs(songs: List[Song]) -> List[Song]:
    unique_songs: List[Song] = []
    for song in songs:
        if not unique_songs.__contains__(song):
            unique_songs.append(song)
    return unique_songs
