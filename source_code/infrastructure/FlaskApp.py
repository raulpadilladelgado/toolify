import os

from flask import Flask

import source_code.infrastructure.main.controller.PlaylistController as PlaylistRoutes


def execute():
    app = Flask(__name__, template_folder="static/templates")
    app.secret_key = os.environ.get('TOOLIFY_SECRET_KEY')
    app.add_url_rule('/', view_func=PlaylistRoutes.login)
    app.add_url_rule('/redirect', view_func=PlaylistRoutes.redirect_page)
    app.add_url_rule('/list', view_func=PlaylistRoutes.list_playlists)
    app.add_url_rule('/order', view_func=PlaylistRoutes.order_playlists, methods=["POST"])
    app.run()