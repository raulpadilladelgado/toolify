from domain.main.entities.Song import Song
from domain.main.services.PlaylistService import PlaylistService


def findDuplicatedSong(songs):
    not_duplicated_songs = list()
    duplicated_songs = list()
    for song in songs:
        if song['track']['name'] in not_duplicated_songs:
            duplicated_songs.append(Song(song['track']['name'], song['track']['id']))
        else:
            not_duplicated_songs.append(song['track']['name'])
    return duplicated_songs if len(duplicated_songs) > 0 else []


class FindDuplicateSong:
    def __init__(self, spotipy, playlist_id):
        self.spotipy = spotipy
        self.playlist_id = playlist_id

    def apply(self):
        playlist_service = PlaylistService(self.spotipy)
        songs = playlist_service.getPlaylistItems(self.playlist_id)
        duplicatedSongs = findDuplicatedSong(songs)
        return duplicatedSongs
