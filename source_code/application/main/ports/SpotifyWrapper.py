from typing import List

from source_code.domain.main.valueobjects.DuplicatedSongs import DuplicatedSongs
from source_code.domain.main.valueobjects.NonRemixSongs import NonRemixSongs
from source_code.domain.main.valueobjects.Playlists import Playlists
from source_code.domain.main.valueobjects.Songs import Songs


class SpotifyWrapper:
    def playlist_add_songs_by(self, playlist_id: str, songs_ids: List[str]) -> None:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def get_count_of_songs_by(self, playlist_id: str) -> int:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def get_songs_by(self, playlist_id: str) -> Songs:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def get_user_playlists(self) -> Playlists:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def replace_songs_by(self, playlist_id: str, songs: Songs) -> None:
        ...

    def remove_specific_song_occurrences(self, playlist_id: str, duplicated_songs: DuplicatedSongs) -> None:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def remove_song_occurrences(self, playlist_id: str, remix_songs: NonRemixSongs) -> None:
        raise NotImplementedError("This method should be implemented by subclasses.")

