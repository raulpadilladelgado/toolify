class AddPlaylistItems:
    def __init__(self, spotipy, playlist_id, songs_ids):
        self.spotipy = spotipy
        self.playlist_id = playlist_id
        self.songs_ids = songs_ids

    def apply(self):
        chunks = split_songs_list_by_chunks(self.songs_ids, 100)
        for i in range(len(chunks)):
            self.spotipy.playlist_add_items(self.playlist_id, chunks[i])


def split_songs_list_by_chunks(song_ids, chunk_size):
    return [song_ids[x:x + chunk_size] for x in range(0, len(song_ids), chunk_size)]
