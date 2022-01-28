import spotipy
from flask import render_template, request, url_for

from source_code.application.main.use_cases.ListUserPlaylists import ListUserPlaylists
from source_code.application.main.use_cases.ReorderPlaylistByReleaseDate import ReorderPlaylist
from source_code.application.main.services.ReorderByReleaseDate import ReorderByReleaseDate
from source_code.infrastructure.main.controller.LoginController import LoginController
from source_code.infrastructure.main.adapters import SpotipyApi

login_controller = LoginController()


def list_playlists():
    token_info = login_controller.get_token_info()
    spotify_client = spotipy.Spotify(auth=token_info['access_token'])
    spotify_client.playlist_reorder_items()
    list_user_playlists = ListUserPlaylists(SpotipyApi(spotify_client))
    user_playlists = list_user_playlists.apply()
    return render_template(
        "index.html",
        playlists=user_playlists,
        order_playlists_url=url_for('order_playlists', _external=True)
    )


def order_playlists():
    token_info = login_controller.get_token_info()
    spotify_client = spotipy.Spotify(auth=token_info['access_token'])
    reorder_playlist = ReorderPlaylist(SpotipyApi(spotify_client),
                                       request.form['playlist'],
                                       ReorderByReleaseDate())
    reorder_playlist.apply()
    return list_playlists()
