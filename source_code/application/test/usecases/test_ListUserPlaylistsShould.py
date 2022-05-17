import unittest
from unittest.mock import Mock

from source_code.application.main.usecases.ListUserPlaylists import ListUserPlaylists
from source_code.domain.main.valueobjects.Playlist import Playlist
from source_code.domain.main.valueobjects.Playlists import Playlists
from source_code.domain.test.fixtures.PlaylistsFixtures import playlists

FAKE_PLAYLIST_NAME = 'PLAYLIST_NAME'

FAKE_PLAYLIST_ID = 'PLAYLIST_ID'

FAKE_PLAYLIST_DESCRIPTION = 'A simple description'

FAKE_PLAYLIST_IMAGE_URI = 'A simple uri'


class test_ListUserPlaylistsShould(unittest.TestCase):
    def test_show_playlists(self):
        fake_playlists = playlists()
        spotipy_wrapper = Mock()
        spotipy_wrapper.get_playlists = Mock(return_value=fake_playlists)
        list_user_playlists = ListUserPlaylists(spotipy_wrapper)

        user_playlists = list_user_playlists.apply()

        self.assertEqual(fake_playlists, user_playlists)
