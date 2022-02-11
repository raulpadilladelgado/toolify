import unittest

from source_code.application.main.services.ReorderByReleaseDate import reorder

FAKE_SONG_ID_TREE = 'SONG_ID_E'

FAKE_SONG_ID_ONE = 'SONG_ID_Z'

FAKE_SONG_ID_TWO = 'SONG_ID_D'


class ReorderByReleaseDateTest(unittest.TestCase):
    def test_reorder_playlists_by_release_date(self):
        items = a_list_of_song_ids_with_distinct_release_dates()

        user_playlists = reorder(items)

        expected_result = [(FAKE_SONG_ID_ONE, '2021-10-14'),
                           (FAKE_SONG_ID_TWO, '2021-10-11'),
                           (FAKE_SONG_ID_TREE, '2021-10-10')]
        self.assertEqual(expected_result, user_playlists)


def a_list_of_song_ids_with_distinct_release_dates():
    return [
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
