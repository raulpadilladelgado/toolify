import unittest
from playlistoperator import PlaylistOperator
from unittest.mock import Mock
import spotipy


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_show_playlists(self):
        spotipy_mock_returned_value = {
            'href': 'https://api.spotify.com/v1/users/11172067860/playlists?offset=0&limit=1', 'items': [
                {'collaborative': False,
                 'description': 'Your weekly mixtape of fresh music. Enjoy new music and deep cuts picked for you. Updates every Monday.',
                 'external_urls': {'spotify': 'https://open.spotify.com/playlist/37i9dQZEVXcWTsLEWE5BJV'},
                 'href': 'https://api.spotify.com/v1/playlists/37i9dQZEVXcWTsLEWE5BJV', 'id': '37i9dQZEVXcWTsLEWE5BJV',
                 'images': [{'height': None,
                             'url': 'https://newjams-images.scdn.co/image/ab676477000033ad/dt/v3/discover-weekly/aAbca4VNfzWuUCQ_FGiEFA==/bmVuZW5lbmVuZW5lbmVuZQ==',
                             'width': None}], 'name': 'Discover Weekly', 'owner': {'display_name': 'Spotify',
                                                                                   'external_urls': {
                                                                                       'spotify': 'https://open.spotify.com/user/spotify'},
                                                                                   'href': 'https://api.spotify.com/v1/users/spotify',
                                                                                   'id': 'spotify', 'type': 'user',
                                                                                   'uri': 'spotify:user:spotify'},
                 'primary_color': None, 'public': False,
                 'snapshot_id': 'MCwwMDAwMDAwMDg0MzVlZGQ0YzI2ZDZjMDliZWE2ZWY1ZDE5NDg2N2Qw',
                 'tracks': {'href': 'https://api.spotify.com/v1/playlists/37i9dQZEVXcWTsLEWE5BJV/tracks', 'total': 30},
                 'type': 'playlist', 'uri': 'spotify:playlist:37i9dQZEVXcWTsLEWE5BJV'}], 'limit': 1,
            'next': 'https://api.spotify.com/v1/users/11172067860/playlists?offset=1&limit=1', 'offset': 0,
            'previous': None, 'total': 10}
        spotipy_mock = spotipy
        spotipy_mock.current_user_playlists = Mock(return_value=spotipy_mock_returned_value)
        playlist_operator = PlaylistOperator(spotipy_mock)

        user_playlists = playlist_operator.list_user_playlists()

        expected_result = 'Discover Weekly - 37i9dQZEVXcWTsLEWE5BJV'
        self.assertEqual(user_playlists, expected_result)
