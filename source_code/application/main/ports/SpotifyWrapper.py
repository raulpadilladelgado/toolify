from source_code.domain.main.valueobjects.Playlists import Playlists
from source_code.domain.main.valueobjects.Songs import Songs


class SpotifyWrapper:
    def __init__(self):
        ...

    def playlist_add_items(self, playlist_id, items):
        ...

    def delete_all_items(self, playlist_id):
        ...

    def get_playlist_items_size(self, playlist_id):
        ...

    def get_playlist_items(self, playlist_id) -> Songs:
        ...

    def get_user_playlists(self) -> Playlists:
        ...

    def __get_user(self):
        ...

    def replace_items(self, playlist_id: str, songs: Songs):
        ...
