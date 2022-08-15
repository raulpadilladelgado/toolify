import unittest
from typing import List, Mapping
from unittest.mock import Mock, call

from source_code.domain.main.valueobjects.DuplicatedSong import DuplicatedSong
from source_code.domain.main.valueobjects.DuplicatedSongs import DuplicatedSongs
from source_code.domain.main.valueobjects.Playlists import Playlists
from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs
from source_code.domain.test.fixtures.PlaylistsFixtures import playlists
from source_code.infrastructure.main.adapters.SpotifyWrapperWithSpotipy import SpotifyWrapperWithSpotipy
from source_code.infrastructure.resources.samples.SampleSinglePlaylistFromSpotipy import sample_playlists
from source_code.infrastructure.resources.samples.SampleSingleUserFromSpotipy import sample_single_user, \
    sample_single_user_no_owner

FAKE_PLAYLIST_ID = "PLAYLIST_ID"


class TestSpotifyWrapperWithSpotipyShould(unittest.TestCase):
    spotify_client = Mock()
    spotify_wrapper: SpotifyWrapperWithSpotipy = SpotifyWrapperWithSpotipy(spotify_client)

    def test_get_playlist_when_the_user_is_owner(self) -> None:
        self.spotify_client.current_user_playlists = Mock(return_value=sample_playlists)
        self.spotify_client.current_user = Mock(return_value=sample_single_user)
        result: Playlists = self.spotify_wrapper.get_user_playlists()
        self.assertEqual(playlists(), result)

    def test_cannot_get_playlist_when_the_user_is_not_owner(self) -> None:
        self.spotify_client.current_user_playlists = Mock(return_value=sample_playlists)
        self.spotify_client.current_user = Mock(return_value=sample_single_user_no_owner)
        result: Playlists = self.spotify_wrapper.get_user_playlists()
        self.assertEqual(Playlists([]), result)

    def test_get_playlist_items_size(self) -> None:
        playlist_info = {
            'tracks': {
                'total': 10
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)
        playlist_items_size = self.spotify_wrapper.get_count_of_songs_by(FAKE_PLAYLIST_ID)
        self.assertEqual(10, playlist_items_size)

    def test_add_more_than_100_items_to_playlist(self) -> None:
        fake_playlist_items = populate_fake_playlist_song_ids_list(200)
        playlist_info = {
            'tracks': {
                'total': 200
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)
        self.spotify_wrapper.playlist_add_songs_by(FAKE_PLAYLIST_ID, fake_playlist_items)
        expected_calls = [call.playlist_add_items(FAKE_PLAYLIST_ID, populate_fake_playlist_song_ids_list(100)),
                          call.playlist_add_items(FAKE_PLAYLIST_ID, populate_fake_playlist_song_ids_list(100))]
        self.spotify_client.playlist_add_items.assert_has_calls(expected_calls)

    def test_add_less_than_100_items_to_playlist(self) -> None:
        fake_playlist_items = populate_fake_playlist_song_ids_list(100)
        playlist_info = {
            'tracks': {
                'total': 100
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)
        self.spotify_wrapper.playlist_add_songs_by(FAKE_PLAYLIST_ID, fake_playlist_items)
        expected_calls = [call.playlist_add_items(FAKE_PLAYLIST_ID, populate_fake_playlist_song_ids_list(100))]
        self.spotify_client.playlist_add_items.assert_has_calls(expected_calls)

    def test_get_less_than_100_items(self) -> None:
        playlist_info = {
            'tracks': {
                'total': 100
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)
        self.spotify_client.playlist_items = Mock(return_value=populate_fake_playlist_items_list(100))
        result = self.spotify_wrapper.get_songs_by(FAKE_PLAYLIST_ID)
        expected_result = populate_songs_list(100)
        self.assertEqual(result, expected_result)

    def test_get_more_than_100_items(self) -> None:
        playlist_info = {
            'tracks': {
                'total': 200
            }
        }
        self.spotify_client.playlist = Mock(return_value=playlist_info)
        self.spotify_client.playlist_items = Mock(return_value=populate_fake_playlist_items_list(100))
        result = self.spotify_wrapper.get_songs_by(FAKE_PLAYLIST_ID)
        expected_result = populate_songs_list(200)
        self.assertEqual(result, expected_result)

    def test_remove_duplicated_songs(self) -> None:
        self.spotify_wrapper.remove_specific_song_occurrences(FAKE_PLAYLIST_ID, some_duplicated_songs())

        expected_calls = [
            call.playlist_remove_specific_occurrences_of_items(
                FAKE_PLAYLIST_ID,
                [
                    {"uri": "1234", "positions": [3, 4]}
                ]
            )
        ]
        self.spotify_client.playlist_remove_specific_occurrences_of_items.assert_has_calls(expected_calls)


def populate_fake_playlist_items_list(size: int) -> Mapping[str, object]:
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
    return Songs.create(populate_song_list(size))


def populate_song_list(size: int) -> List[Song]:
    fake_playlist_items = []
    for _ in range(size):
        fake_playlist_items.append(Song(
            "someName",
            "abc1234",
            ""
        ))
    return fake_playlist_items


def populate_fake_playlist_song_ids_list(size: int) -> List[str]:
    fake_playlist_items = []
    for _ in range(size):
        fake_playlist_items.append("abc1234")
    return fake_playlist_items


def some_duplicated_songs() -> DuplicatedSongs:
    return DuplicatedSongs(
        [
            DuplicatedSong("como sea", "1234", "date", [3, 4])
        ]
    )
