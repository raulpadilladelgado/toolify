class GetPlaylists:
    def __init__(self, spotipy):
        self.spoti_wrapper = spotipy

    def apply(self):
        results = self.spoti_wrapper.get_playlists()
        return results
