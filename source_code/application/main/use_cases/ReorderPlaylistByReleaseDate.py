from source_code.domain.main.services.PlaylistService import PlaylistService


class ReorderPlaylist:
    def __init__(self, spotipy, playlist_id, reorderer):
        self.spotipy = spotipy
        self.playlist_id = playlist_id
        self.reorderer = reorderer

    def apply(self):
        playlist_service = PlaylistService(self.spotipy)
        song = playlist_service.getPlaylistItems(self.playlist_id)
        reordered_song = self.reorderer.execute(song)
        playlist_service.delete_items_in_playlist(self.playlist_id)
        playlist_service.add_items_to_playlist(self.playlist_id, reordered_song)
