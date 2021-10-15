from collections import OrderedDict
from datetime import datetime
import re


def build_pretty_playlists_list(results):
    final_result = ''
    for ixd, item in enumerate(results['items']):
        final_result += item['name'] + " - " + item['id'] + '\n'
    return final_result


def reorder_song_ids(items):
    tracks = dict()
    for i in range(len(items)):
        if re.search("^\d{4}-\d{2}-\d{2}$", items[i]['track']['album']['release_date']):
            tracks[items[i]['track']['id']] = items[i]['track']['album']['release_date']
    reordered_songs = OrderedDict(reversed(sorted(
        tracks.items(),
        key=lambda x: datetime.strptime(x[1], "%Y-%m-%d")
    )))
    return list(reordered_songs.keys())


def split_songs_list_by_chunks_of_100(song_ids):
    return [song_ids[x:x + 100] for x in range(0, len(song_ids), 100)]


class PlaylistOperator:

    def __init__(self, spotipy):
        self.spotipy = spotipy

    def list_user_playlists(self):
        results = self.spotipy.current_user_playlists(10)
        return build_pretty_playlists_list(results)

    def reorder_playlist_by_release_date(self, playlist_id):
        song = self.getPlaylistItems(playlist_id)
        reordered_song = reorder_song_ids(song)
        self.delete_items_in_playlist(playlist_id)
        self.add_items_to_playlist_by_chunks_of_100(playlist_id, reordered_song)

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

    def delete_items_in_playlist(self, playlist_id):
        self.spotipy.playlist_replace_items(playlist_id, [])

    def add_items_to_playlist_by_chunks_of_100(self, playlist_id, song_ids):
        chunks = split_songs_list_by_chunks_of_100(song_ids)
        for i in range(len(chunks)):
            self.spotipy.playlist_add_items(playlist_id, chunks[i])
