from __future__ import annotations

from typing import List, Optional
import re

from source_code.domain.main.valueobjects.NonRemixSong import NonRemixSong
from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs


class RemixSongs(object):
    @classmethod
    def of(cls, songs: Songs) -> Optional[RemixSongs]:
        remix_songs = find_non_remix_songs(songs)
        if remix_songs is None:
            return None
        return RemixSongs(remix_songs)

    def __init__(self, songs: List[NonRemixSong]) -> None:
        self.__songs = songs

    def songs(self) -> List[NonRemixSong]:
        return self.__songs

    def songs_ids(self) -> List[str]:
        return list([song.spotify_id() for song in self.__songs])

    def __eq__(self, o: object) -> bool:
        if isinstance(o, RemixSongs) and len(o.__songs) == len(self.__songs):
            return o.__songs == self.__songs
        return False


def find_non_remix_songs(songs: Songs) -> List[NonRemixSong]:
    remix_songs = filter_remix_songs(songs.songs())
    non_remix_songs = []
    for remix_song in remix_songs:
        for index, song in enumerate(songs.songs()):
            if re.search(song.get_name(), remix_song.get_name(), re.IGNORECASE) \
                    and song.get_name() != remix_song.get_name() \
                    and all(item in remix_song.get_artists() for item in song.get_artists()):
                non_remix_songs.append(
                    NonRemixSong(song.get_name(), song.get_spotify_id(), song.get_release_date())
                )
    return non_remix_songs


def filter_remix_songs(songs: List[Song]) -> List[Song]:
    return list(filter(lambda song: re.search("remix", song.get_name(), re.IGNORECASE), songs))
