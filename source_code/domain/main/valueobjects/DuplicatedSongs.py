from __future__ import annotations

from typing import List, Optional

from source_code.domain.main.valueobjects.DuplicatedSong import DuplicatedSong
from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs


class DuplicatedSongs(object):
    @classmethod
    def of(cls, songs: Songs) -> Optional[DuplicatedSongs]:
        duplicated_songs = find_duplicated_songs(songs)
        if duplicated_songs is None:
            return None
        return DuplicatedSongs(duplicated_songs)

    def __init__(self, duplicated_songs: List[DuplicatedSong]) -> None:
        self.__values = duplicated_songs

    def values(self) -> List[DuplicatedSong]:
        return self.__values

    def __eq__(self, o: object) -> bool:
        if isinstance(o, DuplicatedSongs) and len(o.__values) == len(self.__values):
            return o.__values == self.__values
        return False


def find_duplicated_songs(songs: Songs) -> List[DuplicatedSong]:
    unique_songs = __filter_unique_songs(songs.values())
    all_songs = songs.values()
    return [
        duplicated_song for unique_song in unique_songs
        if (duplicated_song := __get_duplicated_song_from(unique_song, all_songs)) is not None
    ]


def __get_duplicated_song_from(
        unique_song: Song,
        all_songs: List[Song]
) -> Optional[DuplicatedSong]:
    occurrences = __find_song_occurrences(all_songs, unique_song)
    if len(occurrences) <= 1:
        return None
    album_indices = __get_album_indices(all_songs, occurrences)
    single_indices = __get_single_indices(all_songs, occurrences)
    if album_indices:
        duplicate_indices = sorted(single_indices)
    else:
        duplicate_indices = sorted(occurrences[1:])
    if not duplicate_indices:
        return None
    song = all_songs[duplicate_indices[0]]
    return DuplicatedSong(
        song.get_name(),
        song.get_spotify_id(),
        song.get_release_date(),
        duplicate_indices
    )


def __get_single_indices(all_songs: List[Song], occurrences: List[int]) -> set[int]:
    return {idx for idx in occurrences if all_songs[idx].get_album_type() != "album"}


def __get_album_indices(all_songs: List[Song], occurrences: List[int]) -> set[int]:
    return {idx for idx in occurrences if all_songs[idx].get_album_type() == "album"}


def __find_song_occurrences(all_songs: List[Song], unique_song: Song) -> List[int]:
    return [index for index, song in enumerate(all_songs)
            if song.get_name() == unique_song.get_name() and song.get_artists() == unique_song.get_artists()]


def __filter_unique_songs(songs: List[Song]) -> List[Song]:
    unique_songs: List[Song] = []
    for song in songs:
        if not unique_songs.__contains__(song):
            unique_songs.append(song)
    return unique_songs
