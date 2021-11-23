import json
import unittest

from domain.main.services.ReorderByReleaseDate import ReorderByReleaseDate

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


class ReorderByReleaseDateTest(unittest.TestCase):
    def test_reorder_playlists(self):
        items = {
            'items': [
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-10'
                        },
                        'id': FAKE_SONG_ID_TREE
                    }
                },
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-14'
                        },
                        'id': FAKE_SONG_ID_ONE
                    }
                },
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-11'
                        },
                        'id': FAKE_SONG_ID_TWO
                    }
                }
            ]
        }
        reorderer_playlist_by_release_date = ReorderByReleaseDate()

        user_playlists = reorderer_playlist_by_release_date.execute(items['items'])

        expected_result = [FAKE_SONG_ID_ONE, FAKE_SONG_ID_TWO, FAKE_SONG_ID_TREE]
        self.assertEqual(json.dumps(expected_result), json.dumps(user_playlists))
