import unittest
from unittest.mock import Mock, call

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

    def test_add_more_than_100_items_to_playlist(self):
        fake_playlist_items = []
        populate_fake_playlist_items_list(fake_playlist_items)
        populate_fake_playlist_items_list(fake_playlist_items)
        playlist_info = {
            'tracks': {
                'total': 200
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)

        self.spotipy_api.playlist_add_items(self.fake_playlist_id, fake_playlist_items)

        calls = [call.playlist(''),
                 call.playlist_add_items('', populate_fake_playlist_items_list([])),
                 call.playlist_add_items('', populate_fake_playlist_items_list([]))]
        self.spotify_client.assert_has_calls(calls)

def populate_fake_playlist_items_list(fake_playlist_items):
    for _ in range(100):
        fake_playlist_items.append({
            'id': "someID",
            'name': "someName"
        })
    return fake_playlist_items
