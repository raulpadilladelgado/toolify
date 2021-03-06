from unittest import TestCase

from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs


class TestSongs(TestCase):
    def test_reorder_songs(self):
        result = songs_unordered().reorder_by_release_date()
        self.assertEqual("4444", result.songs()[0].get_spotify_id())
        self.assertEqual("1111", result.songs()[1].get_spotify_id())
        self.assertEqual("2222", result.songs()[2].get_spotify_id())
        self.assertEqual("3333", result.songs()[3].get_spotify_id())


def songs_unordered():
    return Songs(
        [
            Song("aguacate", "1111", "2021-10-14"),
            Song("aguacate", "2222", "2021-10-13"),
            Song("aguacate", "3333", "2021-10-10"),
            Song("aguacate", "4444", "2021-10-15")
        ]
    )
