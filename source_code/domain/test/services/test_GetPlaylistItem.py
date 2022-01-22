import unittest
from unittest.mock import Mock

from source_code.domain.main.services.GetPlaylistItems import GetPlaylistItems
from source_code.domain.main.wrappers.SpotipyWrapper import SpotifyWrapper

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


class GetPlaylistItemsTest(unittest.TestCase):

    def test_get_more_than_100_song_with_one_request(self):
        total_tracks_in_playlist = 200
        fake_tracks_info = {
            'tracks':
                {
                    'total': total_tracks_in_playlist
                }
        }
        fake_playlist_items = {
            'items': [

            ]
        }
        populate_fake_playlist_items_list(fake_playlist_items)
        spotipy_mock = Mock()
        spotipy_mock.playlist = Mock(return_value=fake_tracks_info)
        spotipy_mock.playlist_items = Mock(return_value=fake_playlist_items)
        spotipy_mock.playlist_items = Mock(return_value=fake_playlist_items)
        spotify_wrapper = SpotifyWrapper(spotipy_mock)
        get_playlist_items = GetPlaylistItems(spotify_wrapper, FAKE_PLAYLIST_ID)

        items = get_playlist_items.apply()

        self.assertEqual(total_tracks_in_playlist, len(items))


def populate_fake_playlist_items_list(fake_playlist_items):
    for _ in range(100):
        fake_playlist_items['items'].append({
            'id': FAKE_SONG_ID_ONE,
            'name': FAKE_SONG_NAME_ONE
        })
