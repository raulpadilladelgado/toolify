from source_code.application.main.ports.SpotifyWrapper import SpotifyWrapper
from source_code.application.main.services.AddPlaylistItems import AddPlaylistItems
from source_code.application.main.services.DeletePlaylistItems import DeletePlaylistItems
from source_code.application.main.services.GetPlaylistItems import GetPlaylistItems
from source_code.application.main.services.ReorderByReleaseDate import reorder


class ReorderPlaylist:
    def __init__(self, spotipy: SpotifyWrapper, playlist_id: str):
        self.get_playlist_items = GetPlaylistItems(spotipy, playlist_id)
        self.delete_items_in_playlist = DeletePlaylistItems(spotipy, playlist_id)
        self.add_items_to_playlist = AddPlaylistItems(spotipy, playlist_id)

    def apply(self):
        songs = self.get_playlist_items.apply()
        reordered_songs = reorder(songs)
        self.delete_items_in_playlist.apply()
        self.add_items_to_playlist.apply(reordered_songs)
