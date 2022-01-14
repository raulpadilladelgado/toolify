def split_songs_list_by_chunks(song_ids, chunk_size):
    return [song_ids[x:x + chunk_size] for x in range(0, len(song_ids), chunk_size)]


class PlaylistService:
    def __init__(self, spotipy):
        self.spotipy = spotipy

    def getPlaylistItems(self, playlist_id):
        number_of_tracks_in_playlist = self.spotipy.playlist(playlist_id)['tracks']['total']
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

    def delete_items_in_playlist(self, playlist_id):
        self.spotipy.playlist_replace_items(playlist_id, [])

    def add_items_to_playlist(self, playlist_id, song_ids):
        chunks = split_songs_list_by_chunks(song_ids, 100)
        for i in range(len(chunks)):
            self.spotipy.playlist_add_items(playlist_id, chunks[i])

    def get_user_id(self):
        print(self.spotipy.current_user())
