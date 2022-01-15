from source_code.domain.main.services.AddPlaylistItems import AddPlaylistItems
from source_code.domain.main.services.DeletePlaylistItems import DeletePlaylistItems
from source_code.domain.main.services.GetPlaylistItems import GetPlaylistItems


class ReorderPlaylist:
    def __init__(self, spotipy, playlist_id, reorderer):
        self.spotipy = spotipy
        self.playlist_id = playlist_id
        self.reorderer = reorderer

    def apply(self):
        get_playlist_items = GetPlaylistItems(self.spotipy, self.playlist_id)
        song = get_playlist_items.apply()
        reordered_song = self.reorderer.execute(song)
        delete_items_in_playlist = DeletePlaylistItems(self.spotipy, self.playlist_id)
        delete_items_in_playlist.apply()
        add_items_to_playlist = AddPlaylistItems(self.spotipy, self.playlist_id, reordered_song)
        add_items_to_playlist.apply()
