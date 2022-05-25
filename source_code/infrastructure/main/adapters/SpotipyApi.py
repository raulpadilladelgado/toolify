from typing import List

from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.domain.main.valueobjects.Playlist import Playlist
from source_code.domain.main.valueobjects.Playlists import Playlists
from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs


class SpotipyApi(SpotifyWrapper):
    __CHUNK_SIZE = 100

    def __init__(self, spotipy):
        super().__init__()
        self.spotipy = spotipy

    def playlist_add_items(self, playlist_id: str, items: List[str]):
        number_of_tracks_in_playlist = len(items)
        print(f'Tracks in playlist: {number_of_tracks_in_playlist}')
        if number_of_tracks_in_playlist > 100:
            chunks = self.__split_songs_list_by_chunks(items)
            for i in range(len(chunks)):
                print(f'Inserting {len(chunks[i])} songs')
                self.spotipy.playlist_add_items(playlist_id, chunks[i])
        else:
            self.spotipy.playlist_add_items(playlist_id, items)

    def delete_all_items(self, playlist_id):
        self.spotipy.playlist_replace_items(playlist_id, [])

    def get_playlist_items_size(self, playlist_id) -> int:
        playlist = self.spotipy.playlist(playlist_id)
        print(playlist)
        return playlist['tracks']['total']

    def get_playlist_items(self, playlist_id) -> Songs:
        number_of_tracks_in_playlist = self.get_playlist_items_size(playlist_id)
        if number_of_tracks_in_playlist > 100:
            result = []
            counter = 0
            while counter < number_of_tracks_in_playlist:
                result += self.spotipy.playlist_items(playlist_id, offset=counter)['items']
                counter += 100
            return Songs(list(map(lambda x:
                                  Song(
                                      x['track']['name'],
                                      x['track']['id'],
                                      x['track']['album']['release_date']
                                  ), result)))
        return Songs(list(map(lambda x:
                              Song(
                                  x['track']['name'],
                                  x['track']['id'],
                                  x['track']['album']['release_date']
                              ), self.spotipy.playlist_items(playlist_id)['items'])))

    def get_user_playlists(self) -> Playlists:
        playlist_items = self.spotipy.current_user_playlists()['items']
        playlist_items_filtered = self.__filter_playlists_items_by_user(playlist_items)
        return Playlists(
            list(map(lambda playlist_item:
                     Playlist(playlist_item['name'],
                              playlist_item['id'],
                              playlist_item['description'],
                              playlist_item['images'][0]['url'] if playlist_item['images'] else "static/spotify-icon-removebg-preview.png",
                              playlist_item['tracks']['total']
                              ),
                     playlist_items_filtered
                     )
                 )
        )

    def __filter_playlists_items_by_user(self, playlist_items):
        user = self.__get_user()
        return list(filter(lambda playlist_item: playlist_item['owner']['id'] == user, playlist_items))

    def replace_items(self, playlist_id, songs):
        self.delete_all_items(playlist_id)
        self.playlist_add_items(playlist_id, songs.songs_ids())

    def __get_user(self):
        return self.spotipy.current_user()['id']

    def __split_songs_list_by_chunks(self, song_ids):
        return [song_ids[x:x + self.__CHUNK_SIZE] for x in range(0, len(song_ids), self.__CHUNK_SIZE)]
