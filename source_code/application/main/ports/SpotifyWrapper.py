from source_code.domain.main.valueobjects.Playlists import Playlists
from source_code.domain.main.valueobjects.Songs import Songs


class SpotifyWrapper:
    def __init__(self):
        ...

    def playlist_add_songs_by(self, playlist_id: str, songs_ids):
        ...

    def delete_all_songs_by(self, playlist_id: str):
        ...

    def get_count_of_songs_by(self, playlist_id: str):
        ...

    def get_songs_by(self, playlist_id: str) -> Songs:
        ...

    def get_user_playlists(self) -> Playlists:
        ...

    def replace_songs_by(self, playlist_id: str, songs: Songs):
        ...
