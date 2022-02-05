from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper


class GetUserId:
    def __init__(self, spotipy: SpotifyWrapper):
        self.spoti_wrapper = spotipy

    def apply(self):
        user_id = self.spoti_wrapper.get_user()
        return user_id
