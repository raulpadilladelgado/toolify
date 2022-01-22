from source_code.domain.main.wrappers import SpotipyWrapper


class GetPlaylists:
    def __init__(self, spotipy: SpotipyWrapper):
        self.spoti_wrapper = spotipy

    def apply(self):
        results = self.spoti_wrapper.get_playlists()
        return results
