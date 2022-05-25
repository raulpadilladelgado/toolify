import os

from flask import Flask
from source_code.infrastructure.main.controllers import PlaylistController, LoginController

app = Flask(__name__, template_folder="../../static/templates")
app.secret_key = os.environ.get('TOOLIFY_SECRET_KEY')
app.add_url_rule('/', view_func=LoginController.login)
app.add_url_rule('/redirect', view_func=LoginController.redirect_page)
app.add_url_rule('/list', view_func=PlaylistController.list_playlists, methods=["GET"])
app.add_url_rule('/order', view_func=PlaylistController.order_playlists, methods=["POST"])
