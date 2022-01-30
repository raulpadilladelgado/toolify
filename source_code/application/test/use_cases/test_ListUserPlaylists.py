import unittest
from unittest.mock import Mock

from source_code.application.main.use_cases.ListUserPlaylists import ListUserPlaylists
from source_code.domain.main.value_objects.Playlist import Playlist
from source_code.infrastructure.main.adapters.SpotipyApi import SpotipyApi


FAKE_PLAYLIST_NAME = 'PLAYLIST_NAME'

FAKE_PLAYLIST_ID = 'PLAYLIST_ID'

FAKE_PLAYLIST_DESCRIPTION = 'A simple description'

FAKE_PLAYLIST_IMAGE_URI = 'A simple uri'


class ListUserPlaylistsTest(unittest.TestCase):
    def test_show_playlists_when_all_are_user_owner(self):
        fake_playlists_list = {
            'items': [
                {
                    'id': FAKE_PLAYLIST_ID,
                    'name': FAKE_PLAYLIST_NAME,
                    'description': FAKE_PLAYLIST_DESCRIPTION,
                    'images': [
                        {
                            'url': FAKE_PLAYLIST_IMAGE_URI
                        }
                    ],
                    'tracks': {
                        'total': 10
                    },
                    'owner':{
                        'id': '1234'
                    }
                }
            ]
        }
        fake_user = {'id': '1234'}
        spotipy_mock = Mock()
        spotipy_mock.current_user_playlists = Mock(return_value=fake_playlists_list)
        spotipy_mock.current_user = Mock(return_value=fake_user)
        spotify_wrapper = SpotipyApi(spotipy_mock)
        list_user_playlists = ListUserPlaylists(spotify_wrapper)

        user_playlists = list_user_playlists.apply()

        expected_result = [Playlist(
            FAKE_PLAYLIST_NAME,
            FAKE_PLAYLIST_ID,
            FAKE_PLAYLIST_DESCRIPTION,
            FAKE_PLAYLIST_IMAGE_URI,
            10
        )]
        self.assertEqual(expected_result[0].get_name(), user_playlists[0].get_name())
        self.assertEqual(expected_result[0].get_spotify_id(), user_playlists[0].get_spotify_id())

    def test_not_show_playlists_when_all_are_not_user_owner(self):
        fake_playlists_list = {
            'items': [
                {
                    'id': FAKE_PLAYLIST_ID,
                    'name': FAKE_PLAYLIST_NAME,
                    'description': FAKE_PLAYLIST_DESCRIPTION,
                    'images': [
                        {
                            'url': FAKE_PLAYLIST_IMAGE_URI
                        }
                    ],
                    'tracks': {
                        'total': 10
                    },
                    'owner':{
                        'id': '1234'
                    }
                }
            ]
        }
        fake_user = {'id': 'not_user_id'}
        spotipy_mock = Mock()
        spotipy_mock.current_user_playlists = Mock(return_value=fake_playlists_list)
        spotipy_mock.current_user = Mock(return_value=fake_user)
        spotify_wrapper = SpotipyApi(spotipy_mock)
        list_user_playlists = ListUserPlaylists(spotify_wrapper)

        user_playlists = list_user_playlists.apply()

        expected_result = []
        self.assertEqual(expected_result, user_playlists)

