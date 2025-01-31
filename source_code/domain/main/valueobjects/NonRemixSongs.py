from __future__ import annotations

from typing import List, Optional
import re

from source_code.domain.main.valueobjects.NonRemixSong import NonRemixSong
from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs


class NonRemixSongs(object):
    @classmethod
    def of(cls, songs: Songs, keywords: List[str]) -> Optional[NonRemixSongs]:
        remix_songs = find_non_remix_songs(songs, keywords)
        if remix_songs is None:
            return None
        return NonRemixSongs(remix_songs)

    def __init__(self, non_remix_songs: List[NonRemixSong]) -> None:
        self.__values = non_remix_songs

    def values(self) -> List[NonRemixSong]:
        return self.__values

    def songs_ids(self) -> List[str]:
        return list([song.spotify_id() for song in self.__values])

    def __eq__(self, o: object) -> bool:
        if isinstance(o, NonRemixSongs) and len(o.__values) == len(self.__values):
            return o.__values == self.__values
        return False


def find_non_remix_songs(songs: Songs, keywords: List[str]) -> List[NonRemixSong]:
    remix_songs = filter_remix_songs(songs.values(), keywords)
    non_remix_songs = []
    for remix_song in remix_songs:
        for index, song in enumerate(songs.values()):
            if re.search(song.get_name(), remix_song.get_name(), re.IGNORECASE) \
                    and song.get_name() != remix_song.get_name() \
                    and all(item in remix_song.get_artists() for item in song.get_artists()):
                non_remix_songs.append(
                    NonRemixSong(song.get_name(), song.get_spotify_id(), song.get_release_date())
                )
    return non_remix_songs


def filter_remix_songs(songs: List[Song], keywords: List[str]) -> List[Song]:
    return list(filter(lambda song: any(re.search(keyword, song.get_name(), re.IGNORECASE) for keyword in keywords), songs))
