import unittest
from unittest.mock import Mock

from source_code.application.main.usecases.RemoveNonRemixSongs import RemoveNonRemixSongs
from source_code.domain.main.valueobjects.NonRemixSong import NonRemixSong
from source_code.domain.main.valueobjects.NonRemixSongs import NonRemixSongs
from source_code.domain.fixtures.SongsFixtures import some_songs_with_duplicates, some_songs_without_duplicates
from source_code.infrastructure.main.provider.EnvironmentKeywordsProvider import EnvironmentKeywordsProvider

PLAYLIST_ID = "PLAYLIST_ID"


class TestRemoveNonRemixSongsShould(unittest.TestCase):
    def test_find_non_remix_songs_to_be_removed(self) -> None:
        spotify_wrapper = Mock()
        spotify_wrapper.get_songs_by = Mock(return_value=some_songs_with_duplicates())
        keywords_provider = EnvironmentKeywordsProvider()

        RemoveNonRemixSongs(spotify_wrapper, keywords_provider).apply(PLAYLIST_ID)

        expected_non_remix_song_occurrences = NonRemixSongs(
            [
                NonRemixSong("aguacate", "4561", "date")
            ]
        )
        spotify_wrapper.remove_song_occurrences.assert_called_with(PLAYLIST_ID, expected_non_remix_song_occurrences)

    def test_no_non_remix_songs_to_be_removed(self) -> None:
        spotify_wrapper = Mock()
        spotify_wrapper.get_songs_by = Mock(return_value=some_songs_without_duplicates())
        keywords_provider = EnvironmentKeywordsProvider()

        RemoveNonRemixSongs(spotify_wrapper, keywords_provider).apply(PLAYLIST_ID)

        spotify_wrapper.assert_not_called()
