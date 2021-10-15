import unittest
from PlaylistOperator import PlaylistOperator, reorder_song_ids, split_songs_list_by_chunks
from unittest.mock import Mock
import spotipy
import json

FAKE_SONG_ID_TREE = 'SONG_ID_E'

FAKE_SONG_ID_ONE = 'SONG_ID_Z'

FAKE_SONG_ID_TWO = 'SONG_ID_D'

FAKE_PLAYLIST_NAME = 'PLAYLIST_NAME'

FAKE_PLAYLIST_ID = 'PLAYLIST_ID'


class PlaylistOperatorTest(unittest.TestCase):

    def test_show_playlists(self):
        spotipy_mock_returned_value = {
            'items': [
                {
                    'id': FAKE_PLAYLIST_ID,
                    'name': FAKE_PLAYLIST_NAME
                }
            ]
        }
        spotipy_mock = spotipy
        spotipy_mock.current_user_playlists = Mock(return_value=spotipy_mock_returned_value)
        playlist_operator = PlaylistOperator(spotipy_mock)

        user_playlists = playlist_operator.list_user_playlists()

        expected_result = f'{FAKE_PLAYLIST_NAME} - {FAKE_PLAYLIST_ID}\n'
        self.assertEqual(expected_result, user_playlists)

    def test_reorder_playlists(self):
        items = {
            'items': [
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-10'
                        },
                        'id': FAKE_SONG_ID_TREE
                    }
                },
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-14'
                        },
                        'id': FAKE_SONG_ID_ONE
                    }
                },
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-11'
                        },
                        'id': FAKE_SONG_ID_TWO
                    }
                }
            ]
        }

        user_playlists = reorder_song_ids(items['items'])

        expected_result = [FAKE_SONG_ID_ONE, FAKE_SONG_ID_TWO, FAKE_SONG_ID_TREE]
        self.assertEqual(json.dumps(expected_result), json.dumps(user_playlists))

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
        spotipy_mock_returned_value = {
            'tracks':
                {
                    'total': total_tracks_in_playlist
                }
        }
        spotipy_mock_returned_value_2 = {
            'items': [

            ]
        }
        for i in range(100):
            spotipy_mock_returned_value_2['items'].append({
                'id': FAKE_PLAYLIST_ID,
                'name': FAKE_PLAYLIST_NAME
            })

        spotipy_mock = Mock()
        spotipy_mock.playlist = Mock(return_value=spotipy_mock_returned_value)
        spotipy_mock.playlist_items = Mock(return_value=spotipy_mock_returned_value_2)
        playlist_operator = PlaylistOperator(spotipy_mock)
        spotipy_mock.playlist_items = Mock(return_value=spotipy_mock_returned_value_2)

        items = playlist_operator.getPlaylistItems(FAKE_PLAYLIST_ID)

        self.assertEqual(total_tracks_in_playlist, len(items))
