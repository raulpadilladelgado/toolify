import unittest
from unittest.mock import Mock

from source_code.domain.main.services.PlaylistService import split_songs_list_by_chunks, PlaylistService

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


def populateFakePlaylistItemsList(fake_playlist_items):
    for i in range(100):
        fake_playlist_items['items'].append({
            'id': FAKE_SONG_ID_ONE,
            'name': FAKE_SONG_NAME_ONE
        })


class PlaylistServiceTest(unittest.TestCase):

    def test_split_songs_list_by_chunks(self):
        songs_list = []
        for i in range(10):
            songs_list.append(FAKE_SONG_ID_ONE)

        splited_song_list = split_songs_list_by_chunks(songs_list, 2)

        expected_result = [
            [FAKE_SONG_ID_ONE, FAKE_SONG_ID_ONE],
            [FAKE_SONG_ID_ONE, FAKE_SONG_ID_ONE],
            [FAKE_SONG_ID_ONE, FAKE_SONG_ID_ONE],
            [FAKE_SONG_ID_ONE, FAKE_SONG_ID_ONE],
            [FAKE_SONG_ID_ONE, FAKE_SONG_ID_ONE]
        ]
        self.assertEqual(expected_result, splited_song_list)

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
        populateFakePlaylistItemsList(fake_playlist_items)
        spotipy_mock = Mock()
        spotipy_mock.playlist = Mock(return_value=fake_tracks_info)
        spotipy_mock.playlist_items = Mock(return_value=fake_playlist_items)
        spotipy_mock.playlist_items = Mock(return_value=fake_playlist_items)
        playlist_service = PlaylistService(spotipy_mock)

        items = playlist_service.getPlaylistItems(FAKE_PLAYLIST_ID)

        self.assertEqual(total_tracks_in_playlist, len(items))
