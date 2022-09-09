from unittest import TestCase
from unittest.mock import Mock

from source_code.application.main.usecases.ReorderPlaylistByReleaseDate import ReorderPlaylistByReleaseDate
from source_code.domain.fixtures.SongsFixtures import songs_unordered, songs_ordered


class TestReorderPlaylistByReleaseDate(TestCase):
    def test_reorder_playlist(self) -> None:
        spotify_wrapper = Mock()
        spotify_wrapper.get_songs_by = Mock(return_value=songs_unordered())
        ReorderPlaylistByReleaseDate(spotify_wrapper, "PLAYLIST_ID").apply()
        spotify_wrapper.replace_songs_by.assert_called_with("PLAYLIST_ID", songs_ordered())
