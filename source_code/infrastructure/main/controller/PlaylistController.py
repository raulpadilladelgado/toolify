import spotipy
from flask import render_template, request, url_for

from source_code.application.main.use_cases.ListUserPlaylists import ListUserPlaylists
from source_code.application.main.use_cases.ReorderPlaylistByReleaseDate import ReorderPlaylist
from source_code.infrastructure.main.adapters.SpotipyApi import SpotipyApi
from source_code.infrastructure.main.controller.LoginController import LoginController


def list_playlists():
    list_user_playlists = ListUserPlaylists(SpotipyApi(get_spotify_client()))
    user_playlists = list_user_playlists.apply()
    return render_template(
        "index.html",
        playlists=user_playlists,
        order_playlists_url=url_for('order_playlists', _external=True)
    )


def order_playlists():
    reorder_playlist = ReorderPlaylist(SpotipyApi(get_spotify_client()), request.form['playlist'])
    reorder_playlist.apply()
    return list_playlists()


def get_spotify_client():
    token_info = LoginController.get_token_info()
    spotify_client = spotipy.Spotify(auth=token_info['access_token'])
    return spotify_client
