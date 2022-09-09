from unittest import TestCase
from unittest.mock import Mock

from source_code.application.main.usecases.ReorderPlaylistByReleaseDate import ReorderPlaylistByReleaseDate
from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs


class TestReorderPlaylistByReleaseDate(TestCase):
    def test_reorder_playlist(self) -> None:
        spotify_wrapper = Mock()
        spotify_wrapper.get_songs_by = Mock(return_value=songs_unordered())
        ReorderPlaylistByReleaseDate(spotify_wrapper, "PLAYLIST_ID").apply()
        spotify_wrapper.replace_songs_by.assert_called_with("PLAYLIST_ID", songs_ordered())


def songs_unordered() -> Songs:
    return Songs.create(
        [
            Song("aguacate", "1111", "2021-10-14", ["artist_id"]),
            Song("aguacate", "2222", "2021-10-13", ["artist_id"]),
            Song("aguacate", "3333", "2021-10-10", ["artist_id"]),
            Song("aguacate", "4444", "2021-10-15", ["artist_id"])
        ]
    )


def songs_ordered() -> Songs:
    return Songs.create(
        [
            Song("aguacate", "4444", "2021-10-15", ["artist_id"]),
            Song("aguacate", "1111", "2021-10-14", ["artist_id"]),
            Song("aguacate", "2222", "2021-10-13", ["artist_id"]),
            Song("aguacate", "3333", "2021-10-10", ["artist_id"]),

        ]
    )
