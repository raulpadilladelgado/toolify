import unittest
from unittest.mock import Mock

from source_code.application.main.usecases.RemoveDuplicatedSongs import RemoveDuplicatedSongs
from source_code.domain.fixtures.SongsFixtures import some_songs_with_duplicates, some_songs_without_duplicates, \
    some_songs_with_album_duplicate
from source_code.domain.main.valueobjects.DuplicatedSong import DuplicatedSong
from source_code.domain.main.valueobjects.DuplicatedSongs import DuplicatedSongs

PLAYLIST_ID = "PLAYLIST_ID"


class TestRemoveDuplicatedSongsShould(unittest.TestCase):
    def test_find_duplicated_songs_to_be_removed(self) -> None:
        spotify_wrapper = Mock()
        spotify_wrapper.get_songs_by = Mock(return_value=some_songs_with_duplicates())

        RemoveDuplicatedSongs(spotify_wrapper).apply(PLAYLIST_ID)

        expected_song_occurrences = DuplicatedSongs(
            [
                DuplicatedSong("como sea", "1234", "date", [3, 4])
            ]
        )
        spotify_wrapper.remove_specific_song_occurrences.assert_called_with(PLAYLIST_ID, expected_song_occurrences)

    def test_no_songs_to_be_removed(self) -> None:
        spotify_wrapper = Mock()
        spotify_wrapper.get_songs_by = Mock(return_value=some_songs_without_duplicates())

        RemoveDuplicatedSongs(spotify_wrapper).apply(PLAYLIST_ID)

        spotify_wrapper.assert_not_called()

    def test_album_type_prevails_in_duplicates(self) -> None:
        spotify_wrapper = Mock()
        spotify_wrapper.get_songs_by = Mock(return_value=some_songs_with_album_duplicate())

        RemoveDuplicatedSongs(spotify_wrapper).apply(PLAYLIST_ID)

        expected_song_occurrences = DuplicatedSongs(
            [
                DuplicatedSong("como sea", "3456", "date", [1, 4])
            ]
        )
        spotify_wrapper.remove_specific_song_occurrences.assert_called_with(PLAYLIST_ID, expected_song_occurrences)
