import os

from flask import Flask
from flask_session import Session

from source_code.infrastructure.main.controllers import LoginController, PlaylistController

app = Flask(__name__, static_folder="../../static", template_folder="../../static/templates")
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)
app.add_url_rule('/list', view_func=PlaylistController.list_playlists)
app.add_url_rule('/order', view_func=PlaylistController.order_playlists, methods=["POST"])
app.add_url_rule('/remove-duplicated', view_func=PlaylistController.remove_duplicated_songs, methods=["POST"])
app.add_url_rule('/remove-non-remix', view_func=PlaylistController.remove_non_remix_songs, methods=["POST"])
app.add_url_rule('/sign_out', view_func=LoginController.sign_out)
app.add_url_rule('/', view_func=LoginController.login)
