from unittest import TestCase
from unittest.mock import Mock

from source_code.application.main.usecases.ReorderPlaylistByReleaseDate import ReorderPlaylistByReleaseDate
from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs


class TestReorderPlaylistByReleaseDate(TestCase):
    def test_reorder_playlist(self):
        spotify_wrapper = Mock()
        spotify_wrapper.get_playlist_items = Mock(return_value=songs_unordered())

        ReorderPlaylistByReleaseDate(spotify_wrapper, "PLAYLIST_ID").apply()

        spotify_wrapper.replace_items.assert_called_with("PLAYLIST_ID", songs_ordered())


def songs_unordered():
    return Songs(
        [
            Song("aguacate", "1111", "2021-10-14"),
            Song("aguacate", "2222", "2021-10-13"),
            Song("aguacate", "3333", "2021-10-10"),
            Song("aguacate", "4444", "2021-10-15")
        ]
    )


def songs_ordered():
    return Songs(
        [
            Song("aguacate", "4444", "2021-10-15"),
            Song("aguacate", "1111", "2021-10-14"),
            Song("aguacate", "2222", "2021-10-13"),
            Song("aguacate", "3333", "2021-10-10"),

        ]
    )
