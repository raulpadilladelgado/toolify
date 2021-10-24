import os

import flask
import spotipy
from flask import Flask, render_template, request, url_for
from spotipy.oauth2 import SpotifyOAuth

from application.PlaylistOperator import PlaylistOperator

app = Flask(__name__)

scopes = ["playlist-modify-private",
          "playlist-read-private",
          "playlist-modify-public",
          "playlist-read-collaborative"]


@app.route("/")
def list_playlists():
    host_url = flask.request.host_url
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
                                                   client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET'),
                                                   redirect_uri=host_url + 'callback',
                                                   scope=scopes))
    playlist_operator = PlaylistOperator(sp)
    user_playlists = playlist_operator.list_user_playlists()
    return render_template(
        "index.html",
        playlists=user_playlists,
        order_playlists_url=url_for('order_playlists')
    )


@app.route('/order', methods=['POST'])
def order_playlists():
    host_url = flask.request.host_url
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
                                                   client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET'),
                                                   redirect_uri=host_url + 'callback',
                                                   scope=scopes))
    playlist_operator = PlaylistOperator(sp)
    playlist_operator.reorder_playlist_by_release_date(request.form['playlist'])
    return list_playlists()


@app.route('/aguacate')
def aguacate():
    print(flask.request.host_url)
    return render_template('index.html')
