class SpotifyWrapper:
    def __init__(self, spotipy):
        self.spotipy = spotipy

    def playlist_add_items(self, playlist_id, items):
        ...

    def delete_all_items(self, playlist_id):
        ...

    def get_playlist_items_size(self, playlist_id):
        ...

    def get_playlist_items(self, playlist_id):
        ...

    def get_playlists(self):
        ...

    def get_user(self):
        ...
