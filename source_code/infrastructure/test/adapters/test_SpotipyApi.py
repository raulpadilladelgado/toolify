import unittest
from typing import List
from unittest.mock import Mock, call

from source_code.domain.main.valueobjects.Playlists import Playlists
from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs
from source_code.domain.test.fixtures.PlaylistsFixtures import playlists
from source_code.infrastructure.main.adapters.SpotifyWrapperWithSpotipyApi import SpotifyWrapperWithSpotipyApi
from source_code.infrastructure.resources.samples.SampleSinglePlaylistFromSpotipy import sample_playlists
from source_code.infrastructure.resources.samples.SampleSingleUserFromSpotipy import sample_single_user, \
    sample_single_user_no_owner


class TestSpotipyApiShould(unittest.TestCase):
    spotify_client = Mock()
    spotify_wrapper: SpotifyWrapperWithSpotipyApi = SpotifyWrapperWithSpotipyApi(spotify_client)
    fake_playlist_id = ""

    def test_get_playlist_when_the_user_is_owner(self):
        self.spotify_client.current_user_playlists = Mock(return_value=sample_playlists)
        self.spotify_client.current_user = Mock(return_value=sample_single_user)
        result: Playlists = self.spotify_wrapper.get_user_playlists()
        self.assertEqual(playlists(), result)

    def test_cannot_get_playlist_when_the_user_is_not_owner(self):
        self.spotify_client.current_user_playlists = Mock(return_value=sample_playlists)
        self.spotify_client.current_user = Mock(return_value=sample_single_user_no_owner)
        result: Playlists = self.spotify_wrapper.get_user_playlists()
        self.assertEqual(Playlists([]), result)

    def test_get_playlist_items_size(self):
        playlist_info = {
            'tracks': {
                'total': 10
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)
        playlist_items_size = self.spotify_wrapper.get_count_of_songs_by(self.fake_playlist_id)
        self.assertEqual(10, playlist_items_size)

    def test_add_more_than_100_items_to_playlist(self):
        fake_playlist_items = populate_fake_playlist_song_ids_list(200)
        playlist_info = {
            'tracks': {
                'total': 200
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)
        self.spotify_wrapper.playlist_add_songs_by(self.fake_playlist_id, fake_playlist_items)
        expected_calls = [call.playlist_add_items('', populate_fake_playlist_song_ids_list(100)),
                          call.playlist_add_items('', populate_fake_playlist_song_ids_list(100))]
        self.spotify_client.playlist_add_items.assert_has_calls(expected_calls)

    def test_add_less_than_100_items_to_playlist(self):
        fake_playlist_items = populate_fake_playlist_song_ids_list(100)
        playlist_info = {
            'tracks': {
                'total': 100
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)
        self.spotify_wrapper.playlist_add_songs_by(self.fake_playlist_id, fake_playlist_items)
        expected_calls = [call.playlist_add_items('', populate_fake_playlist_song_ids_list(100))]
        self.spotify_client.playlist_add_items.assert_has_calls(expected_calls)

    def test_get_less_than_100_items(self):
        playlist_info = {
            'tracks': {
                'total': 100
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)
        self.spotify_client.playlist_items = Mock(return_value=populate_fake_playlist_items_list(100))
        result = self.spotify_wrapper.get_songs_by(self.fake_playlist_id)
        expected_result = populate_songs_list(100)
        self.assertEqual(result, expected_result)

    def test_get_more_than_100_items(self):
        playlist_info = {
            'tracks': {
                'total': 200
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)
        self.spotify_client.playlist_items = Mock(return_value=populate_fake_playlist_items_list(100))
        result = self.spotify_wrapper.get_songs_by(self.fake_playlist_id)
        expected_result = populate_songs_list(200)
        self.assertEqual(result, expected_result)


def populate_fake_playlist_items_list(size: int):
    fake_playlist_items = []
    for _ in range(size):
        fake_playlist_items.append({
            'track': {
                'album': {
                    'release_date': ''
                },
                "name": "someName",
                'id': 'abc1234'
            },
            'owner': {
                'id': '11172067860'
            }
        })
    fake_playlist_items_2 = {
        'items': fake_playlist_items
    }
    return fake_playlist_items_2


def populate_songs_list(size: int) -> Songs:
    return Songs(populate_song_list(size))


def populate_song_list(size: int) -> List[Song]:
    fake_playlist_items = []
    for _ in range(size):
        fake_playlist_items.append(Song(
            "someName",
            "abc1234",
            ""
        ))
    return fake_playlist_items


def populate_fake_playlist_song_ids_list(size: int):
    fake_playlist_items = []
    for _ in range(size):
        fake_playlist_items.append("abc1234")
    return fake_playlist_items
