class GetPlaylists:
    def __init__(self, spotipy):
        self.spotipy = spotipy

    def apply(self):
        results = self.spotipy.current_user_playlists()
        return results
