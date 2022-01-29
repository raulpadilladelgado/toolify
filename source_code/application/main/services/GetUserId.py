class GetUserId:
    def __init__(self, spotipy):
        self.spotipy = spotipy

    def apply(self):
        user_id = self.spotipy.get_user()
        return user_id
