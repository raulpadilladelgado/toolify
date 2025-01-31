from __future__ import annotations

from typing import List, Dict, Any

from flask import url_for
from spotipy import Spotify

from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.domain.main.valueobjects.DuplicatedSongs import DuplicatedSongs
from source_code.domain.main.valueobjects.NonRemixSongs import NonRemixSongs
from source_code.domain.main.valueobjects.Playlist import Playlist
from source_code.domain.main.valueobjects.Playlists import Playlists
from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs
from source_code.infrastructure.main.dto.PlaylistDto import PlaylistDto

SONGS_ALLOWED_BY_REQUEST = 100


class SpotifyWrapperWithSpotipy(SpotifyWrapper):
    __CHUNK_SIZE = 100

    def __init__(self, spotipy: Spotify):
        super().__init__()
        self.spotipy: Spotify = spotipy

    def playlist_add_songs_by(self, playlist_id: str, songs_ids: List[str]) -> None:
        number_of_songs_in_playlist = len(songs_ids)
        self.__add_songs_by_chunks_of_max_songs_allowed_by_request(playlist_id, songs_ids) \
            if number_of_songs_in_playlist > SONGS_ALLOWED_BY_REQUEST \
            else self.__add_songs(playlist_id, songs_ids)

    def get_count_of_songs_by(self, playlist_id: str) -> int:
        return int(self.spotipy.playlist(playlist_id)['tracks']['total'])

    def get_songs_by(self, playlist_id: str) -> Songs:
        number_of_songs_in_playlist: int = self.get_count_of_songs_by(playlist_id)
        return self.__get_songs_by_chunks_of_max_songs_allowed_by_request(number_of_songs_in_playlist, playlist_id) \
            if number_of_songs_in_playlist > SONGS_ALLOWED_BY_REQUEST \
            else self.__get_songs(playlist_id)

    def get_user_playlists(self) -> Playlists:
        playlists: Playlists = self.__get_playlists_from_items()
        return self.__filter_playlists_by_user(playlists)

    def replace_songs_by(self, playlist_id: str, songs: Songs) -> None:
        self.__delete_all_songs_by(playlist_id)
        self.playlist_add_songs_by(playlist_id, songs.songs_ids())

    def remove_specific_song_occurrences(self, playlist_id: str, duplicated_songs: DuplicatedSongs) -> None:
        self.spotipy.playlist_remove_specific_occurrences_of_items(
            playlist_id,
            from_duplicated_songs_to_items(duplicated_songs)
        )

    def remove_song_occurrences(self, playlist_id: str, remix_songs: NonRemixSongs) -> None:
        self.spotipy.playlist_remove_all_occurrences_of_items(playlist_id, remix_songs.songs_ids())

    def __add_songs(self, playlist_id: str, songs_ids: List[str]) -> None:
        self.spotipy.playlist_add_items(playlist_id, songs_ids)

    def __delete_all_songs_by(self, playlist_id: str) -> None:
        self.spotipy.playlist_replace_items(playlist_id, [])

    def __add_songs_by_chunks_of_max_songs_allowed_by_request(self, playlist_id: str, songs_ids: List[str]) -> None:
        chunks: List[List[str]] = self.__split_songs_by_max_number_of_songs_by_request(songs_ids)
        for i in range(len(chunks)):
            self.spotipy.playlist_add_items(playlist_id, chunks[i])

    def __get_songs(self, playlist_id: str) -> Songs:
        return Songs.create(list(map(lambda x:
                                     Song(
                                         x['track']['name'],
                                         x['track']['id'],
                                         x['track']['album']['release_date'],
                                         list([artist['id'] for artist in x['track']['artists']])
                                     ), self.spotipy.playlist_items(playlist_id)['items'])))

    def __get_songs_by_chunks_of_max_songs_allowed_by_request(self, number_of_songs_in_playlist: int,
                                                              playlist_id: str) -> Songs:
        result = []
        counter: int = 0
        while counter < number_of_songs_in_playlist:
            result += self.spotipy.playlist_items(playlist_id, offset=counter)['items']
            counter += 100
        return Songs.create(list(map(lambda x:
                                     Song(
                                         x['track']['name'],
                                         x['track']['id'],
                                         x['track']['album']['release_date'],
                                         list([artist['id'] for artist in x['track']['artists']])
                                     ), result)))

    def __get_playlists_from_items(self) -> Playlists:
        playlist_items: List[PlaylistDto] = list(
            map(lambda playlist_item: PlaylistDto(playlist_item), self.spotipy.current_user_playlists()['items']))
        if len(playlist_items) <= 0:
            return Playlists([])
        filtered_items = filter(lambda item: item is not None, playlist_items)
        return Playlists(
            list(map(lambda playlist_item:
                     Playlist(playlist_item.name,
                              playlist_item.id,
                              playlist_item.owner_id,
                              playlist_item.description,
                              playlist_item.image_url,
                              playlist_item.total_tracks
                              ), filtered_items)
                 )
        )

    def __filter_playlists_by_user(self, playlists: Playlists) -> Playlists:
        user: str = self.spotipy.current_user()['id']
        return Playlists(list(filter(lambda playlist: playlist.get_user_id() == user, playlists.values())))

    def __split_songs_by_max_number_of_songs_by_request(self, song_ids: List[str]) -> List[List[str]]:
        return [song_ids[x:x + self.__CHUNK_SIZE] for x in range(0, len(song_ids), self.__CHUNK_SIZE)]


def from_duplicated_songs_to_items(duplicated_songs: DuplicatedSongs) -> List[Dict[str, str | List[int]]]:
    items: List[Dict[str, str | List[int]]] = []
    for duplicated_song in duplicated_songs.values():
        items.append(
            {"uri": duplicated_song.spotify_id(), "positions": duplicated_song.positions()}
        )
    return items
