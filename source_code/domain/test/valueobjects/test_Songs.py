from unittest import TestCase

from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs


class TestSongs(TestCase):
    def test_reorder_songs(self) -> None:
        result = songs_unordered().reorder_by_release_date()
        self.assertEqual("4444", result.songs()[0].get_spotify_id())
        self.assertEqual("1111", result.songs()[1].get_spotify_id())
        self.assertEqual("2222", result.songs()[2].get_spotify_id())
        self.assertEqual("3333", result.songs()[3].get_spotify_id())


def songs_unordered() -> Songs:
    return Songs.create(
        [
            Song("aguacate", "1111", "2021-10-14", ["artist_id"]),
            Song("aguacate", "2222", "2021-10-13", ["artist_id"]),
            Song("aguacate", "3333", "2021-10-10", ["artist_id"]),
            Song("aguacate", "4444", "2021-10-15", ["artist_id"])
        ]
    )
