import unittest
from unittest.mock import Mock

from source_code.application.main.usecases.RemoveDuplicatedSongs import RemoveDuplicatedSongs
from source_code.domain.fixtures.DuplicatedSongsFixtures import some_duplicated_songs
from source_code.domain.fixtures.SongsFixtures import some_songs_with_duplicates, some_songs_without_duplicates

PLAYLIST_ID = "PLAYLIST_ID"


class TestRemoveDuplicatedSongsShould(unittest.TestCase):
    def test_find_duplicated_songs_to_be_removed(self) -> None:
        spotify_wrapper = Mock()
        spotify_wrapper.get_songs_by = Mock(return_value=some_songs_with_duplicates())

        RemoveDuplicatedSongs(spotify_wrapper).apply(PLAYLIST_ID)

        expected_song_occurrences = some_duplicated_songs()
        spotify_wrapper.remove_specific_song_occurrences.assert_called_with(PLAYLIST_ID, expected_song_occurrences)

    def test_no_songs_to_be_removed(self) -> None:
        spotify_wrapper = Mock()
        spotify_wrapper.get_songs_by = Mock(return_value=some_songs_without_duplicates())

        RemoveDuplicatedSongs(spotify_wrapper).apply(PLAYLIST_ID)

        spotify_wrapper.assert_not_called()
