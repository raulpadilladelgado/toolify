class DeletePlaylistItems:
    def __init__(self, spotipy, playlist_id):
        self.spotipy = spotipy
        self.playlist_id = playlist_id

    def apply(self):
        self.spotipy.playlist_replace_items(self.playlist_id, [])
