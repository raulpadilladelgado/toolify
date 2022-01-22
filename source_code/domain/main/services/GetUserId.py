from source_code.domain.main.wrappers import SpotipyWrapper


class GetUserId:
    def __init__(self, spotipy: SpotipyWrapper):
        self.spotipy = spotipy

    def apply(self):
        user_id = self.spotipy.get_user()
        return user_id
