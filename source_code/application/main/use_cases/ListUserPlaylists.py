from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.domain.main.value_objects.Playlist import Playlist
from source_code.application.main.services.GetPlaylists import GetPlaylists
from source_code.application.main.services.GetUserId import GetUserId


class ListUserPlaylists:
    def __init__(self, spotipy: SpotifyWrapper):
        self.spotipy = spotipy
        self.get_playlists = GetPlaylists(spotipy)
        self.get_user_id = GetUserId(spotipy)

    def apply(self):
        results = self.get_playlists.apply()
        user_id = self.get_user_id.apply()
        return transform_items_to_playlists(results, user_id)


def transform_items_to_playlists(results, user_id):
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
