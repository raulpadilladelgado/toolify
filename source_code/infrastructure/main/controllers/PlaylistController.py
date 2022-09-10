from flask import render_template, request, url_for, redirect

from source_code.application.main.usecases.ListUserPlaylists import ListUserPlaylists
from source_code.application.main.usecases.RemoveDuplicatedSongs import RemoveDuplicatedSongs
from source_code.application.main.usecases.RemoveNonRemixSongs import RemoveNonRemixSongs
from source_code.application.main.usecases.ReorderPlaylistByReleaseDate import ReorderPlaylistByReleaseDate
from source_code.infrastructure.main.adapters.SpotifyWrapperWithSpotipy import SpotifyWrapperWithSpotipy
from source_code.infrastructure.main.controllers.LoginController import get_client


def list_playlists():
    client = get_client()
    user_is_not_logged = client is None
    if user_is_not_logged:
        return redirect(url_for('login'))
    playlists = ListUserPlaylists(SpotifyWrapperWithSpotipy(client)).apply()
    return render_template(
        "index.html",
        playlists=playlists.values(),
        list_playlists_url=url_for('list_playlists'),
        order_playlists_url=url_for('order_playlists'),
        remove_duplicated_songs_url=url_for('remove_duplicated_songs'),
        remove_non_remix_songs_url=url_for('remove_non_remix_songs'),
        sign_out_url=url_for('sign_out')
    )


def order_playlists():
    client = get_client()
    user_is_not_logged = client is None
    if user_is_not_logged:
        return redirect(url_for('login'))
    ReorderPlaylistByReleaseDate(SpotifyWrapperWithSpotipy(client), request.form['playlist']).apply()
    return "OK"


def remove_duplicated_songs():
    client = get_client()
    user_is_not_logged = client is None
    if user_is_not_logged:
        return redirect(url_for('login'))
    RemoveDuplicatedSongs(SpotifyWrapperWithSpotipy(client)).apply(request.form['playlist'])
    return "OK"


def remove_non_remix_songs():
    client = get_client()
    user_is_not_logged = client is None
    if user_is_not_logged:
        return redirect(url_for('login'))
    RemoveNonRemixSongs(SpotifyWrapperWithSpotipy(client)).apply(request.form['playlist'])
    return "OK"
