from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.application.main.services.GetPlaylistItems import GetPlaylistItems
from source_code.domain.main.value_objects.Song import Song


class FindDuplicateSong:
    def __init__(self, spotipy: SpotifyWrapper, playlist_id: str):
        self.spotipy = spotipy
        self.playlist_id = playlist_id

    def apply(self):
        get_playlist_items = GetPlaylistItems(self.spotipy, self.playlist_id)
        songs = get_playlist_items.apply()
        duplicated_songs = find_duplicated_song(songs)
        return duplicated_songs


def find_duplicated_song(songs):
    not_duplicated_songs = list()
    duplicated_songs = list()
    for song in songs:
        if song['track']['name'] in not_duplicated_songs:
            duplicated_songs.append(Song(song['track']['name'], song['track']['id']))
        else:
            not_duplicated_songs.append(song['track']['name'])
    return duplicated_songs if len(duplicated_songs) > 0 else []
