import unittest
from PlaylistOperator import PlaylistOperator
from unittest.mock import Mock
import spotipy
import json

FAKE_SONG_ID_TREE = 'SONG_ID_E'

FAKE_SONG_ID_ONE = 'SONG_ID_Z'

FAKE_SONG_ID_TWO = 'SONG_ID_D'

FAKE_PLAYLIST_NAME = 'PLAYLIST_NAME'

FAKE_PLAYLIST_ID = 'PLAYLIST_ID'


class PlaylistOperatorTest(unittest.TestCase):

    def test_show_playlists(self):
        spotipy_mock_returned_value = {
            'items': [
                {
                    'id': FAKE_PLAYLIST_ID,
                    'name': FAKE_PLAYLIST_NAME
                }
            ]
        }
        spotipy_mock = spotipy
        spotipy_mock.current_user_playlists = Mock(return_value=spotipy_mock_returned_value)
        playlist_operator = PlaylistOperator(spotipy_mock)

        user_playlists = playlist_operator.list_user_playlists()

        expected_result = f'{FAKE_PLAYLIST_NAME} - {FAKE_PLAYLIST_ID}\n'
        self.assertEqual(expected_result, user_playlists)

    def test_reorder_playlists(self):
        spotipy_mock_returned_value = {
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
        spotipy_mock_returned_value_2 = {
            'tracks': {
                'total': 3
            }
        }
        spotipy_mock = spotipy
        spotipy_mock.playlist_items = Mock(return_value=spotipy_mock_returned_value)
        spotipy_mock.playlist = Mock(return_value=spotipy_mock_returned_value_2)
        spotipy_mock.playlist_replace_items = Mock()
        playlist_operator = PlaylistOperator(spotipy_mock)

        user_playlists = playlist_operator.reorder_playlist_by_release_date('PLAYLIST_ID')

        expected_result = '{\"SONG_ID_Z\": \"2021-10-14\", ' \
                          '\"SONG_ID_D\": \"2021-10-11\", ' \
                          '\"SONG_ID_E\": \"2021-10-10\"}'
        self.assertEqual(expected_result, json.dumps(user_playlists))
