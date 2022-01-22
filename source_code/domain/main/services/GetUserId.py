class GetUserId:
    def __init__(self, spotipy):
        self.spotipy = spotipy

    def apply(self):
        user_id = self.spotipy.current_user()
        return user_id['id']
