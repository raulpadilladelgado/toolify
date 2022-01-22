import string

from source_code.domain.main.wrappers import SpotipyWrapper


class GetPlaylistItems:
    def __init__(self, spotipy: SpotipyWrapper, playlist_id: string):
        self.spoti_wrapper = spotipy
        self.playlist_id = playlist_id

    def apply(self):
        items = self.spoti_wrapper.get_playlist_items(self.playlist_id)
        return items
