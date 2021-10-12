import spotipy
from spotipy.oauth2 import SpotifyOAuth

from credentials import Credentials

scopes = ["playlist-modify-private",
          "playlist-read-private",
          "playlist-modify-public",
          "playlist-read-collaborative"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Credentials.SPOTIFY_CLIENT_SECRET,
                                               client_secret=Credentials.SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=Credentials.SPOTIFY_REDIRECT_URI,
                                               scope=scopes))
operation = '0'


def print_main_menu():
    print("+------------------------+")
    print('|What you need to do?    |')
    print('|0 => List user playlists|')
    print('|-1 => Exit              |')
    print("+------------------------+")


def list_user_playlists():
    results = sp.current_user_playlists(10)
    for ixd, item in enumerate(results['items']):
        print(item['name'] + " - " + item['id'])


while operation != '-1':
    print_main_menu()
    operation = input()
    if operation == '0':
        list_user_playlists()
