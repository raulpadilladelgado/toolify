from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper


class GetPlaylists:
    def __init__(self, spotipy: SpotifyWrapper):
        self.spoti_wrapper = spotipy

    def apply(self):
        results = self.spoti_wrapper.get_playlists()
        return results
