import spotipy
from spotipy.oauth2 import SpotifyOAuth
from credentials import Credentials
from playlistoperator import PlaylistOperator

scopes = ["playlist-modify-private",
          "playlist-read-private",
          "playlist-modify-public",
          "playlist-read-collaborative"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Credentials.SPOTIFY_CLIENT_ID,
                                               client_secret=Credentials.SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=Credentials.SPOTIFY_REDIRECT_URI,
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
        print(playlist_operator.reorder_playlist(playlist_id))
