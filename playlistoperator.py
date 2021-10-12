class PlaylistOperator:
    def __init__(self, spotipy):
        self.spotipy = spotipy

    def list_user_playlists(self):
        results = self.spotipy.current_user_playlists(1)
        print(type(results))
        print(results)
        final_result = ''
        for ixd, item in enumerate(results['items']):
            print(item['name'] + " - " + item['id'])
            final_result = item['name'] + " - " + item['id']
        return final_result

    def reorder_playlist(self, playlist_id):
        items = self.spotipy.playlist_items(playlist_id, 'items', 2)
        print(type(items['items']))
        print(items['items'][0]['track']['name'])
        print(items['items'][0]['track']['uri'])
        print(items['items'][0]['track']['id'])
        print(items['items'][0]['track']['album']['release_date'])
        tracks = dict()
        tracks[items['items'][0]['track']['id']] = items['items'][0]['track']['album']['release_date']
        print(tracks)
