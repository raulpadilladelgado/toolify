import unittest
from unittest.mock import Mock

from source_code.application.main.usecases.RemoveDuplicatedSongs import RemoveDuplicatedSongs
from source_code.domain.main.valueobjects.DuplicatedSong import DuplicatedSong
from source_code.domain.main.valueobjects.DuplicatedSongs import DuplicatedSongs
from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs

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
        spotify_wrapper.get_songs_by = Mock(return_value=some_songs_without_duplicatates())

        RemoveDuplicatedSongs(spotify_wrapper).apply(PLAYLIST_ID)

        spotify_wrapper.assert_not_called()


def some_songs_with_duplicates() -> Songs:
    return Songs.create(
        [
            Song("aguacate", "4561", "date"),
            Song("como sea", "1234", "date"),
            Song("aguacate xD", "7894", "date"),
            Song("como sea", "1234", "date"),
            Song("como sea", "1234", "date")
        ]
    )


def some_songs_without_duplicatates() -> Songs:
    return Songs.create(
        [
            Song("aguacate", "4561", "date"),
            Song("como sea", "1234", "date"),
            Song("aguacate xD", "7894", "date"),
        ]
    )
