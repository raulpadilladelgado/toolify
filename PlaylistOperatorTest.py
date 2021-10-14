import unittest
from PlaylistOperator import PlaylistOperator
from unittest.mock import Mock
import spotipy


class PlaylistOperatorTest(unittest.TestCase):

    def test_show_playlists(self):
        spotipy_mock_returned_value = {
            'items': [
                {
                    'id': 'PLAYLIST_ID',
                    'name': 'PLAYLIST_NAME'
                }
            ]
        }
        spotipy_mock = spotipy
        spotipy_mock.current_user_playlists = Mock(return_value=spotipy_mock_returned_value)
        playlist_operator = PlaylistOperator(spotipy_mock)

        user_playlists = playlist_operator.list_user_playlists()

        expected_result = 'PLAYLIST_NAME - PLAYLIST_ID\n'
        self.assertEqual(user_playlists, expected_result)

    def test_reorder_playlists(self):
        spotipy_mock_returned_value = {
            'items': [
                {
                    'track': {
                        'album': {
                            'release_date': 'RELEASE_DATE'
                        },
                        'id': 'PLAYLIST_ID'
                    }
                }
            ]
        }
        spotipy_mock = spotipy
        spotipy_mock.playlist_items = Mock(return_value=spotipy_mock_returned_value)
        playlist_operator = PlaylistOperator(spotipy_mock)

        user_playlists = playlist_operator.reorder_playlist('Playlist ID')

        expected_result = {'PLAYLIST_ID': 'RELEASE_DATE'}
        self.assertEqual(user_playlists, expected_result)
