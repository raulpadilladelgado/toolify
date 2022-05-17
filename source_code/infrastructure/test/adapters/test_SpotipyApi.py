import unittest
from unittest.mock import Mock, call

from source_code.domain.main.valueobjects.Playlists import Playlists
from source_code.domain.test.fixtures.PlaylistsFixtures import playlists
from source_code.infrastructure.main.adapters.SpotipyApi import SpotipyApi
from source_code.infrastructure.resources.samples.SampleSinglePlaylistFromSpotipy import sample_playlists


class SpotipyApiTest(unittest.TestCase):
    spotify_client = Mock()
    spotipy_api: SpotipyApi = SpotipyApi(spotify_client)
    fake_playlist_id = ""

    def test_get_playlist_for_a_user(self):
        self.spotify_client.current_user_playlists = Mock(return_value=sample_playlists)
        self.spotify_client.current_user = Mock(return_value='11172067860')

        result: Playlists = self.spotipy_api.get_user_playlists()

        expected_result = playlists()
        self.assertEqual(expected_result, result)

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

        expected_calls = [call.playlist_add_items('', populate_fake_playlist_items_list([])),
                          call.playlist_add_items('', populate_fake_playlist_items_list([]))]
        self.spotify_client.playlist_add_items.assert_has_calls(expected_calls)

    def test_add_less_than_100_items_to_playlist(self):
        fake_playlist_items = []
        populate_fake_playlist_items_list(fake_playlist_items)
        playlist_info = {
            'tracks': {
                'total': 100
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)

        self.spotipy_api.playlist_add_items(self.fake_playlist_id, fake_playlist_items)

        expected_calls = [call.playlist_add_items('', populate_fake_playlist_items_list([]))]
        self.spotify_client.playlist_add_items.assert_has_calls(expected_calls)

    def test_get_less_than_100_items(self):
        playlist_info = {
            'tracks': {
                'total': 100
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)
        playlist_items = {
            'items': []
        }
        playlist_items['items'] = populate_fake_playlist_items_list(playlist_items['items'])
        self.spotify_client.playlist_items = Mock(return_value=playlist_items)

        result = self.spotipy_api.get_playlist_items(self.fake_playlist_id)

        expected_result = populate_fake_playlist_items_list([])
        self.assertEqual(expected_result, result)

    def test_get_more_than_100_items(self):
        playlist_info = {
            'tracks': {
                'total': 200
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)
        playlist_items = {
            'items': []
        }
        playlist_items['items'] = populate_fake_playlist_items_list(playlist_items['items'])
        self.spotify_client.playlist_items = Mock(return_value=playlist_items)

        result = self.spotipy_api.get_playlist_items(self.fake_playlist_id)

        expected_result = populate_fake_playlist_items_list(populate_fake_playlist_items_list([]))
        self.assertEqual(expected_result, result)


def populate_fake_playlist_items_list(fake_playlist_items):
    for _ in range(100):
        fake_playlist_items.append({
            'id': "someID",
            'name': "someName",
            'track': {
                'id': '',
                'album': {
                    'release_date': ''
                }
            }
        })
    return fake_playlist_items
