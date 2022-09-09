import unittest
from typing import Optional

from source_code.domain.main.valueobjects.NonRemixSong import NonRemixSong
from source_code.domain.main.valueobjects.NonRemixSongs import RemixSongs
from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs


class TestRemoveRemixSongsShould(unittest.TestCase):
    def test_find_remix_songs_to_be_removed(self) -> None:
        remix_songs: Optional[RemixSongs] = RemixSongs.of(some_songs_with_remix())

        expected_songs: RemixSongs = RemixSongs([
            NonRemixSong("aguacate", "4561", "date")
        ])
        self.assertEqual(remix_songs, expected_songs)


def some_songs_with_remix() -> Songs:
    return Songs.create(
        [
            Song("aguacate", "4561", "date", ["suso"]),
            Song("como sea", "1234", "date", ["mingo"]),
            Song("aguacate remix", "7894", "date", ["suso", "maria"]),
            Song("aguacate", "6759", "date", ["juan"]),
        ]
    )
