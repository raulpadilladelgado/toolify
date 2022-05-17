import spotipy
from flask import render_template, request, url_for

from source_code.application.main.usecases.ListUserPlaylists import ListUserPlaylists
from source_code.application.main.usecases.ReorderPlaylistByReleaseDate import ReorderPlaylist
from source_code.infrastructure.main.adapters.SpotipyApi import SpotipyApi
from source_code.infrastructure.main.controller.LoginController import LoginController


def list_playlists():
    return render_template(
        "index.html",
        playlists=ListUserPlaylists(SpotipyApi(get_spotify_client())).apply().playlist_items(),
        order_playlists_url=url_for('order_playlists', _external=True)
    )


def order_playlists():
    ReorderPlaylist(SpotipyApi(get_spotify_client()), request.form['playlist']).apply()
    return list_playlists()


def get_spotify_client():
    access_token = LoginController.get_token_info()['access_token']
    return spotipy.Spotify(auth=access_token)
