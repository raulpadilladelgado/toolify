from source_code.domain.main.entities.Playlist import Playlist


class ListUserPlaylists:
    def __init__(self, spotipy):
        self.spotipy = spotipy

    def apply(self):
        results = self.spotipy.current_user_playlists()
        final_result = []
        for ixd, item in enumerate(results['items']):
            final_result.append(Playlist(
                item['name'],
                item['id'],
                item['description'],
                item['images'][0]['url'],
                item['tracks']['total']
            ))
        return final_result
