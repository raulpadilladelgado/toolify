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
    unique_songs = filter_unique_songs(songs.values())
    duplicated_songs = []
    all_songs = songs.values()
    for unique_song in unique_songs:
        song_occurrences = [index for index, song in enumerate(all_songs)
                            if song.get_name() == unique_song.get_name() and song.get_artists() == unique_song.get_artists()]
        if len(song_occurrences) > 1:
            # Identificar todos los indices de album y no-album
            album_indices = set(idx for idx in song_occurrences if all_songs[idx].get_album_type() == "album")
            non_album_indices = set(idx for idx in song_occurrences if all_songs[idx].get_album_type() != "album")
            if album_indices:
                duplicate_indices = sorted(non_album_indices)
            else:
                # Si no hay album, los duplicados son todos menos el primero
                duplicate_indices = sorted(song_occurrences[1:])
            if duplicate_indices:
                song = all_songs[duplicate_indices[0]]
                duplicated_songs.append(
                    DuplicatedSong(song.get_name(), song.get_spotify_id(), song.get_release_date(), duplicate_indices)
                )
    return duplicated_songs


def filter_unique_songs(songs: List[Song]) -> List[Song]:
    unique_songs: List[Song] = []
    for song in songs:
        if not unique_songs.__contains__(song):
            unique_songs.append(song)
    return unique_songs
