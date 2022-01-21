import unittest
from unittest.mock import Mock

from source_code.application.main.use_cases.FindDuplicateSong import FindDuplicateSong
from source_code.domain.main.value_objects.Song import Song

FAKE_SONG_ID_TREE = 'SONG_ID_E'

FAKE_SONG_NAME_TREE = 'Sandia'

FAKE_SONG_ID_ONE = 'SONG_ID_Z'

FAKE_SONG_NAME_ONE = 'Aguacate'

FAKE_SONG_ID_TWO = 'SONG_ID_D'

FAKE_SONG_NAME_TWO = 'Melon'

FAKE_PLAYLIST_NAME = 'PLAYLIST_NAME'

FAKE_PLAYLIST_ID = 'PLAYLIST_ID'

FAKE_PLAYLIST_DESCRIPTION = 'A simple description'

FAKE_PLAYLIST_IMAGE_URI = 'A simple uri'


class FindDuplicatedSongTest(unittest.TestCase):
    def test_find_duplicate_songs(self):
        spotipy_mock = Mock()
        fake_tracks_info = {
            'tracks':
                {
                    'total': 2
                }
        }
        items = {
            'items': [
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-10'
                        },
                        'id': FAKE_SONG_ID_ONE,
                        'name': FAKE_SONG_NAME_ONE
                    }
                },
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-10'
                        },
                        'id': FAKE_SONG_ID_ONE,
                        'name': FAKE_SONG_NAME_ONE
                    }
                },
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-10'
                        },
                        'id': FAKE_SONG_ID_TWO,
                        'name': FAKE_SONG_NAME_TWO
                    }
                },
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-10'
                        },
                        'id': FAKE_SONG_ID_TWO,
                        'name': FAKE_SONG_NAME_TWO
                    }
                }
            ]
        }
        spotipy_mock.playlist = Mock(return_value=fake_tracks_info)
        spotipy_mock.playlist_items = Mock(return_value=items)
        find_duplicated_song = FindDuplicateSong(spotipy_mock, FAKE_PLAYLIST_ID)

        result = find_duplicated_song.apply()

        expected_result = [Song(FAKE_SONG_NAME_ONE, FAKE_SONG_ID_ONE),
                           Song(FAKE_SONG_NAME_TWO, FAKE_SONG_ID_TWO)]
        self.assertEqual(expected_result[0].get_name(), result[0].get_name())
        self.assertEqual(expected_result[1].get_name(), result[1].get_name())
        self.assertEqual(2, len(result))
