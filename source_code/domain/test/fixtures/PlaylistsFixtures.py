from source_code.domain.main.valueobjects.Playlist import Playlist
from source_code.domain.main.valueobjects.Playlists import Playlists

FAKE_PLAYLIST_NAME = 'PLAYLIST_NAME'

FAKE_PLAYLIST_ID = 'PLAYLIST_ID'

FAKE_PLAYLIST_DESCRIPTION = 'A simple description'

FAKE_PLAYLIST_IMAGE_URI = 'A simple uri'

FAKE_USER_ID = '11172067860'


def playlists() -> Playlists:
    return Playlists(
        [
            Playlist(
                FAKE_PLAYLIST_NAME,
                FAKE_PLAYLIST_ID,
                FAKE_USER_ID,
                FAKE_PLAYLIST_DESCRIPTION,
                FAKE_PLAYLIST_IMAGE_URI,
                10
            )
        ]
    )
