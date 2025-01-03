import json
import os
import uuid

import spotipy
from flask import session, request, redirect, render_template

scopes = ["playlist-modify-private",
          "playlist-read-private",
          "playlist-read-collaborative",
          "playlist-modify-public"]

caches_folder = './.spotify_caches/'
if not os.path.exists(caches_folder):
    os.makedirs(caches_folder)


def login(post_login_action=lambda: redirect('/list')):
    if not session.get('uuid'):
        session['uuid'] = str(uuid.uuid4())
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope=scopes,
                                               cache_path=__session_cache_path(),
                                               show_dialog=False)
    if request.args.get("code"):
        auth_manager.get_access_token(request.args.get("code"))
        return post_login_action()
    if not auth_manager.get_cached_token():
        auth_url = auth_manager.get_authorize_url()
        return render_template(
            "not_logged.html",
            auth_url=auth_url
        )
    return post_login_action()


def sign_out():
    try:
        os.remove(__session_cache_path())
        session.clear()
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    return redirect('/')


def get_auth_tokens():
    return login(lambda: __read_tokens_from_cache_file())


def __session_cache_path():
    return caches_folder + session.get('uuid')


def __read_tokens_from_cache_file() -> any:
    cache_path = __session_cache_path()
    if os.path.exists(cache_path):
        with open(cache_path, 'r') as cache_file:
            token_info = json.load(cache_file)
            access_token = token_info.get('access_token')
            refresh_token = token_info.get('refresh_token')
            tokens = {
                "access_token": access_token,
                "refresh_token": refresh_token
            }
            print(json.dumps(tokens, indent=4))
            return tokens
    else:
        print("Cache file does not exist.")
        return None


def get_client():
    if not session.get('uuid'):
        return None
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope=scopes, cache_path=__session_cache_path())
    return None if not auth_manager.get_cached_token() else spotipy.Spotify(
        auth_manager=auth_manager)
