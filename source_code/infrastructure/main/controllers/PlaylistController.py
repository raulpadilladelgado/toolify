from __future__ import annotations

import multiprocessing

from flask import render_template, request, url_for, redirect, Response
from spotipy import Spotify, SpotifyOAuth

from source_code.application.main.usecases.ListUserPlaylists import ListUserPlaylists
from source_code.application.main.usecases.RemoveDuplicatedSongs import RemoveDuplicatedSongs
from source_code.application.main.usecases.RemoveNonRemixSongs import RemoveNonRemixSongs
from source_code.application.main.usecases.ReorderPlaylistByReleaseDate import ReorderPlaylistByReleaseDate
from source_code.infrastructure.main.adapters.SpotifyWrapperWithSpotipy import SpotifyWrapperWithSpotipy
from source_code.infrastructure.main.controllers.LoginController import get_client


def list_playlists():
    client = get_spotipy_client()
    user_is_not_logged = client is None
    if user_is_not_logged:
        return redirect(url_for('login'))
    playlists = list_user_playlists(client)
    return render_template(
        "index.html",
        playlists=playlists.values(),
        list_playlists_url=url_for('list_playlists'),
        order_playlists_url=url_for('order_playlists'),
        remove_duplicated_songs_url=url_for('remove_duplicated_songs'),
        remove_non_remix_songs_url=url_for('remove_non_remix_songs'),
        sign_out_url=url_for('sign_out')
    )


def get_spotipy_client():
    return get_client()


def list_user_playlists(client):
    return ListUserPlaylists(SpotifyWrapperWithSpotipy(client)).apply()


def order_playlists(build_client = lambda: client_or_redirect_to_login()):
    client = build_client()
    playlist_id = request.form['playlist']
    process = multiprocessing.Process(target=order_playlists_in_background, args=(client, playlist_id))
    process.start()
    return "OK"


def order_playlists_in_background(client, playlist_id):
    ReorderPlaylistByReleaseDate(SpotifyWrapperWithSpotipy(client), playlist_id).apply()


def remove_duplicated_songs():
    client = client_or_redirect_to_login()
    playlist_id = request.form['playlist']
    process = multiprocessing.Process(target=remove_duplicated_songs_in_background, args=(client, playlist_id))
    process.start()
    return "OK"


def remove_duplicated_songs_in_background(client, playlist_id):
    RemoveDuplicatedSongs(SpotifyWrapperWithSpotipy(client)).apply(playlist_id)


def remove_non_remix_songs():
    client = client_or_redirect_to_login()
    playlist_id = request.form['playlist']
    process = multiprocessing.Process(target=remove_non_remix_songs_in_background, args=(client, playlist_id))
    process.start()
    return "OK"


def remove_non_remix_songs_in_background(client, playlist_id):
    RemoveNonRemixSongs(SpotifyWrapperWithSpotipy(client)).apply(playlist_id)


def client_or_redirect_to_login() -> Spotify | Response:
    client: Spotify = get_spotipy_client()
    user_is_not_logged = client is None
    if user_is_not_logged:
        return redirect(url_for('login'))
    return client

def order_playlist_with_auth_token():
    refresh_token = request.form['refresh_token']
    sp_oauth = SpotifyOAuth()
    new_token_info = sp_oauth.refresh_access_token(refresh_token)
    new_access_token = new_token_info['access_token']
    return order_playlists(lambda: Spotify(auth=new_access_token))