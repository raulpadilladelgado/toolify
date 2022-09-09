from typing import Optional

from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.application.main.usecases.RemoveDuplicatedSongs import RemoveDuplicatedSongs
from source_code.domain.main.valueobjects.NonRemixSongs import RemixSongs
from source_code.domain.main.valueobjects.Songs import Songs


class KeepSongsRemixVersion:
    def __init__(self, spotify_wrapper: SpotifyWrapper):
        self.spotify_wrapper = spotify_wrapper

    def apply(self, playlist_id: str) -> None:
        RemoveDuplicatedSongs(self.spotify_wrapper).apply(playlist_id)
        songs: Songs = self.spotify_wrapper.get_songs_by(playlist_id)
        remix_songs: Optional[RemixSongs] = RemixSongs.of(songs)
        if remix_songs is not None:
            self.spotify_wrapper.remove_song_occurrences(playlist_id, remix_songs)
