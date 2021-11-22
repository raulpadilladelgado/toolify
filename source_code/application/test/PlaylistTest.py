import json
import unittest
from unittest.mock import Mock

from application.main.use_cases.FindDuplicateSong import FindDuplicateSong
from application.main.use_cases.ListUserPlaylists import ListUserPlaylists
from domain.main.entities.Playlist import Playlist
from domain.main.entities.Song import Song
from domain.main.services.PlaylistService import split_songs_list_by_chunks, PlaylistService
from domain.main.services.ReorderByReleaseDate import ReorderByReleaseDate

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


class PlaylistOperatorTest(unittest.TestCase):

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
        reorderer_playlist_by_release_date = ReorderByReleaseDate()

        user_playlists = reorderer_playlist_by_release_date.execute(items['items'])

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

    def test_find_duplicate_songs(self):
        spotipy_mock = Mock()
        fake_tracks_info = {
            'tracks':
                {
                    'total': 2
                }
        }
        items = {
            'items': [
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-10'
                        },
                        'id': FAKE_SONG_ID_ONE,
                        'name': FAKE_SONG_NAME_ONE
                    }
                },
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-10'
                        },
                        'id': FAKE_SONG_ID_ONE,
                        'name': FAKE_SONG_NAME_ONE
                    }
                },
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-10'
                        },
                        'id': FAKE_SONG_ID_TWO,
                        'name': FAKE_SONG_NAME_TWO
                    }
                },
                {
                    'track': {
                        'album': {
                            'release_date': '2021-10-10'
                        },
                        'id': FAKE_SONG_ID_TWO,
                        'name': FAKE_SONG_NAME_TWO
                    }
                }
            ]
        }
        spotipy_mock.playlist = Mock(return_value=fake_tracks_info)
        spotipy_mock.playlist_items = Mock(return_value=items)
        find_duplicated_song = FindDuplicateSong(spotipy_mock, FAKE_PLAYLIST_ID)

        result = find_duplicated_song.apply()

        expected_result = [Song(FAKE_SONG_NAME_ONE, FAKE_SONG_ID_ONE),
                           Song(FAKE_SONG_NAME_TWO, FAKE_SONG_ID_TWO)]
        self.assertEqual(expected_result[0].get_name(), result[0].get_name())
        self.assertEqual(expected_result[1].get_name(), result[1].get_name())
        self.assertEqual(2, len(result))
