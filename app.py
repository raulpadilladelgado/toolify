import os
import time
import spotipy
from flask import Flask, render_template, request, url_for, redirect, session
from spotipy.oauth2 import SpotifyOAuth
from application.PlaylistOperator import PlaylistOperator

app = Flask(__name__)
scopes = ["playlist-modify-private",
          "playlist-read-private",
          "playlist-modify-public",
          "playlist-read-collaborative"]
TOKEN_INFO = "token_info"
app.secret_key = os.environ.get('TOOLIFY_SECRET_KEY')


@app.route("/")
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@app.route('/redirect')
def redirect_page():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('list_playlists', _external=True))


@app.route("/list")
def list_playlists():
    try:
        token_info = get_token()
    except:
        print('user not logged in')
        redirect('/')
    sp = spotipy.Spotify(auth=token_info['access_token'])
    playlist_operator = PlaylistOperator(sp)
    user_playlists = playlist_operator.list_user_playlists()
    return render_template(
        "index.html",
        playlists=user_playlists,
        order_playlists_url=url_for('order_playlists', _external=True)
    )


@app.route('/order', methods=['POST'])
def order_playlists():
    try:
        token_info = get_token()
    except:
        print('user not logged in')
        redirect('/')
    sp = spotipy.Spotify(auth=token_info['access_token'])
    playlist_operator = PlaylistOperator(sp)
    playlist_operator.reorder_playlist_by_release_date(request.form['playlist'])
    return list_playlists()


def create_spotify_oauth():
    return SpotifyOAuth(client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
                        client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET'),
                        redirect_uri=url_for('redirect_page', _external=True),
                        scope=scopes)


def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise "exception"
    now = int(time.time())
    is_expired = token_info['expires_at'] - now
    if is_expired:
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        return token_info
