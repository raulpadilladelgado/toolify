import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from application.PlaylistOperator import PlaylistOperator

scopes = ["playlist-modify-private",
          "playlist-read-private",
          "playlist-modify-public",
          "playlist-read-collaborative"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
                                               client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET'),
                                               redirect_uri=os.environ.get('SPOTIFY_REDIRECT_URI'),
                                               scope=scopes))

playlist_operator = PlaylistOperator(sp)


operation = '0'


def print_main_menu():
    print("+------------------------+")
    print('|What you need to do?    |')
    print('|0 => List user playlists|')
    print('|1 => Sort user playlists|')
    print('|-1 => Exit              |')
    print("+------------------------+")


while operation != '-1':
    print_main_menu()
    operation = input()
    if operation == '0':
        print(playlist_operator.list_user_playlists())
    if operation == '1':
        print('Please, type a valid playlist URL:')
        playlist_id = input()
        playlist_operator.reorder_playlist_by_release_date(playlist_id)
        print('Playlist was ordered successfully')
