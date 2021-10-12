def build_pretty_list(results):
    final_result = ''
    for ixd, item in enumerate(results['items']):
        print(item['name'] + " - " + item['id'])
        final_result = item['name'] + " - " + item['id']
    return final_result


class PlaylistOperator:
    def __init__(self, spotipy):
        self.spotipy = spotipy

    def list_user_playlists(self):
        results = self.spotipy.current_user_playlists(1)
        return build_pretty_list(results)

    def reorder_playlist(self, playlist_id):
        items = self.spotipy.playlist_items(playlist_id, 'items', 2)
        tracks = dict()
        tracks[items['items'][0]['track']['id']] = items['items'][0]['track']['album']['release_date']
        return tracks
