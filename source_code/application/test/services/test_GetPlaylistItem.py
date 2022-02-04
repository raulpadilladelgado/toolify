import unittest
from unittest.mock import Mock

from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.application.main.services.GetPlaylistItems import GetPlaylistItems

FAKE_SONG_ID_ONE = 'SONG_ID_Z'

FAKE_SONG_NAME_ONE = 'Aguacate'

FAKE_PLAYLIST_ID = 'PLAYLIST_ID'


class GetPlaylistItemsTest(unittest.TestCase):

    def test_get_song_in_a_request(self):
        fake_playlist_items = []

        populate_fake_playlist_items_list(fake_playlist_items)
        spotify_wrapper = Mock(SpotifyWrapper)
        spotify_wrapper.get_playlist_items = Mock(return_value=fake_playlist_items)
        get_playlist_items = GetPlaylistItems(spotify_wrapper, FAKE_PLAYLIST_ID)

        items = get_playlist_items.apply()

        total_tracks_in_playlist = 200
        self.assertEqual(total_tracks_in_playlist, len(items))


def populate_fake_playlist_items_list(fake_playlist_items):
    for _ in range(200):
        fake_playlist_items.append({
            'id': FAKE_SONG_ID_ONE,
            'name': FAKE_SONG_NAME_ONE
        })
