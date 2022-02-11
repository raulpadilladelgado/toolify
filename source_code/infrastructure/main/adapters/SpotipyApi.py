from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper


class SpotipyApi(SpotifyWrapper):
    __CHUNK_SIZE = 100

    def __init__(self, spotipy):
        super().__init__()
        self.spotipy = spotipy

    def playlist_add_items(self, playlist_id, items):
        number_of_tracks_in_playlist = self.get_playlist_items_size(playlist_id)
        if number_of_tracks_in_playlist > 100:
            chunks = self.__split_songs_list_by_chunks(items)
            for i in range(len(chunks)):
                self.spotipy.playlist_add_items(playlist_id, chunks[i])
        self.spotipy.playlist_add_items(playlist_id, items)

    def delete_all_items(self, playlist_id):
        self.spotipy.playlist_replace_items(playlist_id, [])

    def get_playlist_items_size(self, playlist_id):
        return self.spotipy.playlist(playlist_id)['tracks']['total']

    def get_playlist_items(self, playlist_id):
        number_of_tracks_in_playlist = self.get_playlist_items_size(playlist_id)
        items = self.__get_playlist_items_by_batch(number_of_tracks_in_playlist, playlist_id)
        return items

    def get_playlists(self):
        results = self.spotipy.current_user_playlists()
        return results['items']

    def get_user(self):
        user_id = self.spotipy.current_user()
        return user_id['id']

    def __get_playlist_items_by_batch(self, number_of_tracks_in_playlist, playlist_id):
        if number_of_tracks_in_playlist > 100:
            result = []
            counter = 0
            while counter < number_of_tracks_in_playlist:
                playlist_items = self.spotipy.playlist_items(playlist_id, 'items', None, counter)
                result += playlist_items['items']
                counter += 100
            return result
        items = self.spotipy.playlist_items(playlist_id, 'items')['items']
        return items

    def __split_songs_list_by_chunks(self, song_ids):
        return [song_ids[x:x + self.__CHUNK_SIZE] for x in range(0, len(song_ids), self.__CHUNK_SIZE)]
