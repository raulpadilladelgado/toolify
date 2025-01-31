from typing import Dict, Any

from flask import url_for


class PlaylistDto:
    def __init__(self, items: Dict[str, Any]):
        self.name = items['name']
        self.id = items['id']
        self.description = items['description']
        self.owner_id = items['owner']['id']
        self.total_tracks = items['tracks']['total']
        self.image_url = items['images'][0]['url'] if items['images'] else url_for('static',
                                                                                   filename='images/spotify-icon-removebg-preview.png')