import unittest
from unittest.mock import Mock

from application.main.use_cases.ListUserPlaylists import ListUserPlaylists
from domain.main.entities.Playlist import Playlist

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


class ListUserPlaylistsTest(unittest.TestCase):
    def test_show_playlists(self):
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
                    }
                }
            ]
        }
        spotipy_mock = Mock()
        spotipy_mock.current_user_playlists = Mock(return_value=fake_playlists_list)
        list_user_playlists = ListUserPlaylists(spotipy_mock)

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
