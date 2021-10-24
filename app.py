import os

import spotipy
from flask import Flask, render_template, request, url_for
from spotipy.oauth2 import SpotifyOAuth

from application.PlaylistOperator import PlaylistOperator

app = Flask(__name__)

scopes = ["playlist-modify-private",
          "playlist-read-private",
          "playlist-modify-public",
          "playlist-read-collaborative"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
                                               client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET'),
                                               redirect_uri=os.environ.get('SPOTIFY_REDIRECT_URI'),
                                               scope=scopes))

playlist_operator = PlaylistOperator(sp)


@app.route("/")
def list_playlists():
    user_playlists = playlist_operator.list_user_playlists()
    return render_template(
        "index.html",
        playlists=user_playlists,
        order_playlists_url=url_for('order_playlists')
    )


@app.route('/order', methods=['POST'])
def order_playlists():
    playlist_operator.reorder_playlist_by_release_date(request.form['playlist'])
    return list_playlists()
