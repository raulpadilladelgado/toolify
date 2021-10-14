import unittest
from playlistoperator import PlaylistOperator
from unittest.mock import Mock
import spotipy


class MyTestCase(unittest.TestCase):

    def test_show_playlists(self):
        spotipy_mock_returned_value = {
            'href': 'https://api.spotify.com/v1/users/11172067860/playlists?offset=0&limit=1', 'items': [
                {'id': '37i9dQZEVXcWTsLEWE5BJV',
                 'name': 'Discover Weekly'}]}
        spotipy_mock = spotipy
        spotipy_mock.current_user_playlists = Mock(return_value=spotipy_mock_returned_value)
        playlist_operator = PlaylistOperator(spotipy_mock)

        user_playlists = playlist_operator.list_user_playlists()

        expected_result = 'Discover Weekly - 37i9dQZEVXcWTsLEWE5BJV\n'
        self.assertEqual(user_playlists, expected_result)

    def test_reorder_playlists(self):
        # tracks[items['items'][i]['track']['id']] = items['items'][i]['track']['album']['release_date']
        spotipy_mock_returned_value = {
            'items': [{'track': {
                'album': {'release_date': '2021-09-30'}, 'id': '493Rk3iS7rs8uPfpnfm95u'}}]}
        spotipy_mock = spotipy
        spotipy_mock.playlist_items = Mock(return_value=spotipy_mock_returned_value)
        playlist_operator = PlaylistOperator(spotipy_mock)

        user_playlists = playlist_operator.reorder_playlist('Playlist ID')

        expected_result = {'493Rk3iS7rs8uPfpnfm95u': '2021-09-30'}
        self.assertEqual(user_playlists, expected_result)
