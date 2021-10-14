def build_pretty_playlists_list(results):
    final_result = ''
    for ixd, item in enumerate(results['items']):
        final_result += item['name'] + " - " + item['id'] + '\n'
    return final_result


def build_pretty_items_list(items):
    tracks = dict()
    for i in range(len(items)):
        tracks[items[i]['track']['id']] = items[i]['track']['album']['release_date']
    return tracks


class PlaylistOperator:
    def __init__(self, spotipy):
        self.spotipy = spotipy

    def list_user_playlists(self):
        results = self.spotipy.current_user_playlists(10)
        return build_pretty_playlists_list(results)

    def reorder_playlist(self, playlist_id):
        items = self.spotipy.playlist_items(playlist_id, 'items', 1)
        return build_pretty_items_list(items['items'])
