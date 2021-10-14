from collections import OrderedDict
from datetime import datetime
from itertools import islice
import re


def build_pretty_playlists_list(results):
    final_result = ''
    for ixd, item in enumerate(results['items']):
        final_result += item['name'] + " - " + item['id'] + '\n'
    return final_result


def reorder_songs_by_release_date(items):
    tracks = dict()
    for i in range(len(items)):
        if re.search("^\d{4}-\d{2}-\d{2}$", items[i]['track']['album']['release_date']):
            tracks[items[i]['track']['id']] = items[i]['track']['album']['release_date']
    return OrderedDict(reversed(sorted(
        tracks.items(),
        key=lambda x: datetime.strptime(x[1], "%Y-%m-%d")
    )))


def group_elements(lst, chunk_size):
    lst = iter(lst)
    return iter(lambda: tuple(islice(lst, chunk_size)), ())


class PlaylistOperator:

    def __init__(self, spotipy):
        self.spotipy = spotipy

    def list_user_playlists(self):
        results = self.spotipy.current_user_playlists(10)
        return build_pretty_playlists_list(results)

    def reorder_playlist_by_release_date_2(self, playlist_id):
        items = self.spotipy.playlist_items(playlist_id, 'items')
        reordered_songs = reorder_songs_by_release_date(items['items'])
        return reordered_songs

    def reorder_playlist_by_release_date(self, playlist_id):
        items = self.getPlaylistItems(playlist_id)
        reordered_songs = reorder_songs_by_release_date(items)
        self.spotipy.playlist_replace_items(playlist_id, list(reordered_songs.keys()))
        return reordered_songs

    def getPlaylistItems(self, playlist_id):
        number_of_tracks_in_playlist = self.spotipy.playlist(playlist_id)['tracks']['total']
        if number_of_tracks_in_playlist > 100:
            result = []
            counter = 0
            while counter < number_of_tracks_in_playlist:
                playlist_items = self.spotipy.playlist_items(playlist_id, 'items', None, counter)
                result += playlist_items['items']
                counter += 100
            return result
        items = self.spotipy.playlist_items(playlist_id, 'items')['items']
        return items
