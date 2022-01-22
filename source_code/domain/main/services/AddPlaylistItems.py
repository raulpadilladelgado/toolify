import array
import string

from source_code.domain.main.wrappers.SpotipyWrapper import SpotifyWrapper


class AddPlaylistItems:
    def __init__(self, spotipy: SpotifyWrapper, playlist_id: string, songs_ids: array):
        self.spoti_wrapper = spotipy
        self.playlist_id = playlist_id
        self.songs_ids = songs_ids

    def apply(self):
        chunks = split_songs_list_by_chunks(self.songs_ids, 100)
        self.spoti_wrapper.playlist_add_items(self.playlist_id, chunks)


def split_songs_list_by_chunks(song_ids, chunk_size):
    return [song_ids[x:x + chunk_size] for x in range(0, len(song_ids), chunk_size)]
