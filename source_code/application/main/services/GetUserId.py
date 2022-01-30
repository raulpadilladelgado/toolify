from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper


class GetUserId:
    def __init__(self, spotipy: SpotifyWrapper):
        self.spotipy = spotipy

    def apply(self):
        user_id = self.spotipy.get_user()
        return user_id
