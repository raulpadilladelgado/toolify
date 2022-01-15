class GetPlaylistItems:
    def __init__(self, spotipy, playlist_id):
        self.spotipy = spotipy
        self.playlist_id = playlist_id

    def apply(self):
        number_of_tracks_in_playlist = self.spotipy.playlist(self.playlist_id)['tracks']['total']
        if number_of_tracks_in_playlist > 100:
            result = []
            counter = 0
            while counter < number_of_tracks_in_playlist:
                playlist_items = self.spotipy.playlist_items(self.playlist_id, 'items', None, counter)
                result += playlist_items['items']
                counter += 100
            return result
        items = self.spotipy.playlist_items(self.playlist_id, 'items')['items']
        return items
