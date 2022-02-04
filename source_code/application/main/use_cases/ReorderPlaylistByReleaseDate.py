from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.application.main.services.AddPlaylistItems import AddPlaylistItems
from source_code.application.main.services.DeletePlaylistItems import DeletePlaylistItems
from source_code.application.main.services.GetPlaylistItems import GetPlaylistItems
from source_code.application.main.services.ReorderByReleaseDate import execute


class ReorderPlaylist:
    def __init__(self, spotipy: SpotifyWrapper, playlist_id: str):
        self.spotipy = spotipy
        self.playlist_id = playlist_id

    def apply(self):
        get_playlist_items = GetPlaylistItems(self.spotipy, self.playlist_id)
        song = get_playlist_items.apply()
        reordered_song = execute(song)
        delete_items_in_playlist = DeletePlaylistItems(self.spotipy, self.playlist_id)
        delete_items_in_playlist.apply()
        add_items_to_playlist = AddPlaylistItems(self.spotipy, self.playlist_id, reordered_song)
        add_items_to_playlist.apply()
