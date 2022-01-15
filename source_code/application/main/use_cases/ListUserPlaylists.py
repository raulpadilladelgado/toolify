from source_code.domain.main.value_objects.Playlist import Playlist


class ListUserPlaylists:
    def __init__(self, spotipy):
        self.spotipy = spotipy

    def apply(self):
        results = self.spotipy.current_user_playlists()
        user_id = self.spotipy.current_user()['id']
        final_result = []
        for ixd, item in enumerate(results['items']):
            if item['owner']['id'] == user_id:
                final_result.append(Playlist(
                    item['name'],
                    item['id'],
                    item['description'],
                    item['images'][0]['url'],
                    item['tracks']['total']
                ))
        return final_result
