from __future__ import annotations

from typing import List, Dict

from flask import url_for

from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.domain.main.valueobjects.DuplicatedSongs import DuplicatedSongs
from source_code.domain.main.valueobjects.NonRemixSongs import RemixSongs
from source_code.domain.main.valueobjects.Playlist import Playlist
from source_code.domain.main.valueobjects.Playlists import Playlists
from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs
from spotipy import Spotify


class SpotifyWrapperWithSpotipy(SpotifyWrapper):
    __CHUNK_SIZE = 100

    def __init__(self, spotipy: Spotify):
        super().__init__()
        self.spotipy: Spotify = spotipy

    def playlist_add_songs_by(self, playlist_id: str, songs_ids: List[str]) -> None:
        number_of_tracks_in_playlist = len(songs_ids)
        if number_of_tracks_in_playlist > 100:
            chunks = self.__split_songs_list_by_chunks(songs_ids)
            for i in range(len(chunks)):
                self.spotipy.playlist_add_items(playlist_id, chunks[i])
        else:
            self.spotipy.playlist_add_items(playlist_id, songs_ids)

    def delete_all_songs_by(self, playlist_id: str) -> None:
        self.spotipy.playlist_replace_items(playlist_id, [])

    def get_count_of_songs_by(self, playlist_id: str) -> int:
        return int(self.spotipy.playlist(playlist_id)['tracks']['total'])

    def get_songs_by(self, playlist_id: str) -> Songs:
        number_of_tracks_in_playlist: int = self.get_count_of_songs_by(playlist_id)
        return \
            self.get_playlists_100_by_100(number_of_tracks_in_playlist, playlist_id) \
                if number_of_tracks_in_playlist > 100 \
                else self.get_playlists(playlist_id)

    def get_playlists(self, playlist_id: str) -> Songs:
        return Songs.create(list(map(lambda x:
                                     Song(
                                         x['track']['name'],
                                         x['track']['id'],
                                         x['track']['album']['release_date'],
                                         list([artist['id'] for artist in x['track']['artists']])
                                     ), self.spotipy.playlist_items(playlist_id)['items'])))

    def get_playlists_100_by_100(self, number_of_tracks_in_playlist: int, playlist_id: str) -> Songs:
        result = []
        counter: int = 0
        while counter < number_of_tracks_in_playlist:
            result += self.spotipy.playlist_items(playlist_id, offset=counter)['items']
            counter += 100
        return Songs.create(list(map(lambda x:
                                     Song(
                                         x['track']['name'],
                                         x['track']['id'],
                                         x['track']['album']['release_date'],
                                         list([artist['id'] for artist in x['track']['artists']])
                                     ), result)))

    def get_user_playlists(self) -> Playlists:
        playlists: Playlists = self.get_playlists_from_api_items()
        return self.filter_playlists_items_by_user(playlists)

    def get_playlists_from_api_items(self) -> Playlists:
        playlist_items = self.spotipy.current_user_playlists()['items']
        if len(playlist_items) <= 0:
            return Playlists([])
        return Playlists(
            list(map(lambda playlist_item:
                     Playlist(playlist_item['name'],
                              playlist_item['id'],
                              playlist_item['owner']['id'],
                              playlist_item['description'],
                              playlist_item['images'][0]['url'] if playlist_item[
                                  'images'] else url_for('static', filename='images/spotify-icon-removebg-preview.png'),
                              playlist_item['tracks']['total']
                              ),
                     playlist_items
                     )
                 )
        )

    def filter_playlists_items_by_user(self, playlists: Playlists) -> Playlists:
        user: str = self.spotipy.current_user()['id']
        return Playlists(list(filter(lambda playlist: playlist.get_user_id() == user, playlists.playlist_items())))

    def replace_songs_by(self, playlist_id: str, songs: Songs) -> None:
        self.delete_all_songs_by(playlist_id)
        self.playlist_add_songs_by(playlist_id, songs.songs_ids())

    def remove_specific_song_occurrences(self, playlist_id: str, duplicated_songs: DuplicatedSongs) -> None:
        self.spotipy.playlist_remove_specific_occurrences_of_items(
            playlist_id,
            from_duplicated_song_to_items(duplicated_songs)
        )

    def remove_song_occurrences(self, playlist_id: str, remix_songs: RemixSongs) -> None:
        self.spotipy.playlist_remove_all_occurrences_of_items(playlist_id, remix_songs.songs_ids())

    def __split_songs_list_by_chunks(self, song_ids: List[str]) -> List[List[str]]:
        return [song_ids[x:x + self.__CHUNK_SIZE] for x in range(0, len(song_ids), self.__CHUNK_SIZE)]


def from_duplicated_song_to_items(duplicated_songs: DuplicatedSongs) -> List[Dict[str, str | List[int]]]:
    items: List[Dict[str, str | List[int]]] = []
    for duplicated_song in duplicated_songs.songs():
        items.append(
            {"uri": duplicated_song.spotify_id(), "positions": duplicated_song.positions()}
        )
    return items
