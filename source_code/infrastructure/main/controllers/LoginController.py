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


def session_cache_path():
    return caches_folder + session.get('uuid')


def login():
    if not session.get('uuid'):
        session['uuid'] = str(uuid.uuid4())
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope=scopes,
                                               cache_path=session_cache_path(),
                                               show_dialog=True)
    if request.args.get("code"):
        auth_manager.get_access_token(request.args.get("code"))
        return redirect('/list')
    if not auth_manager.get_cached_token():
        auth_url = auth_manager.get_authorize_url()
        return render_template(
            "not_logged.html",
            auth_url=auth_url
        )
    return redirect('/list')


def sign_out():
    try:
        os.remove(session_cache_path())
        session.clear()
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    return redirect('/')


def get_client():
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope=scopes, cache_path=session_cache_path())
    return None if not auth_manager.get_cached_token() else spotipy.Spotify(
        auth_manager=auth_manager)
