import unittest
from unittest.mock import Mock

from source_code.infrastructure.main.adapters.SpotipyApi import SpotipyApi


class SpotipyApiTest(unittest.TestCase):
    spotify_client = Mock()
    spotipy_api: SpotipyApi = SpotipyApi(spotify_client)
    fake_playlist_id = ""

    def test_get_playlist_items_size(self):
        playlist_info = {
                'tracks': {
                    'total': 10
                }
            }
        self.spotify_client.playlist = Mock(return_value=playlist_info)

        playlist_items_size = self.spotipy_api.get_playlist_items_size(self.fake_playlist_id)

        expected_result = 10
        self.assertEqual(expected_result, playlist_items_size)

