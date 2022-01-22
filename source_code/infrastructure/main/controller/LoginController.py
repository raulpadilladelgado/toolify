import os
import time

from flask import request, url_for, redirect, session
from spotipy.oauth2 import SpotifyOAuth

from source_code.infrastructure.main.exceptions.LoginError import LoginError

scopes = ["playlist-modify-private",
          "playlist-read-private"]

TOKEN_INFO = "token_info"


class LoginController:

    def get_token_info(self):
        try:
            return get_token()
        except LoginError:
            return redirect(url_for('login', _external=True))


def create_spotify_oauth():
    return SpotifyOAuth(client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
                        client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET'),
                        redirect_uri=url_for('redirect_page', _external=True),
                        scope=scopes)


def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


def redirect_page():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('list_playlists', _external=True))


def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise LoginError("Not token info is found")
    now = int(time.time())
    is_expired = token_info['expires_at'] - now
    if is_expired:
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        return token_info
    return token_info['access_token']
