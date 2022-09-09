from typing import List

from source_code.domain.main.valueobjects.DuplicatedSongs import DuplicatedSongs
from source_code.domain.main.valueobjects.NonRemixSongs import RemixSongs
from source_code.domain.main.valueobjects.Playlists import Playlists
from source_code.domain.main.valueobjects.Songs import Songs


class SpotifyWrapper:
    def playlist_add_songs_by(self, playlist_id: str, songs_ids: List[str]) -> None:
        ...

    def get_count_of_songs_by(self, playlist_id: str) -> int:
        ...

    def get_songs_by(self, playlist_id: str) -> Songs:
        ...

    def get_user_playlists(self) -> Playlists:
        ...

    def replace_songs_by(self, playlist_id: str, songs: Songs) -> None:
        ...

    def remove_specific_song_occurrences(self, playlist_id: str, duplicated_songs: DuplicatedSongs) -> None:
        ...

    def remove_song_occurrences(self, playlist_id: str, remix_songs: RemixSongs) -> None:
        ...
