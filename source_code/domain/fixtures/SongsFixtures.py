from source_code.domain.main.valueobjects.Song import Song
from source_code.domain.main.valueobjects.Songs import Songs


def some_songs_with_duplicates() -> Songs:
    return Songs.create(
        [
            Song("aguacate", "4561", "date", ["artist_id"], "single"),
            Song("como sea", "1234", "date", ["artist_id"], "single"),
            Song("aguacate remix", "7894", "date", ["artist_id", "artist_2_id"], "single"),
            Song("como sea", "1234", "date", ["artist_id"], "single"),
            Song("como sea", "1234", "date", ["artist_id"], "single"),
            Song("como sea", "3457", "date", ["artist_3_id"], "single")
        ]
    )


def some_songs_with_album_duplicate() -> Songs:
    return Songs.create(
        [
            Song("aguacate", "4561", "date", ["artist_id"], "single"),
            Song("como sea", "3456", "date", ["artist_id"], "single"),
            Song("aguacate remix", "7894", "date", ["artist_id", "artist_2_id"], "single"),
            Song("como sea", "1234", "date", ["artist_id"], "album"),
            Song("como sea", "3456", "date", ["artist_id"], "single"),
            Song("como sea", "3457", "date", ["artist_3_id"], "single")
        ]
    )


def some_songs_without_duplicates() -> Songs:
    return Songs.create(
        [
            Song("aguacate", "4561", "date", ["artist_id"], "single"),
            Song("como sea", "1234", "date", ["artist_id"], "single"),
            Song("aguacate xD", "7894", "date", ["artist_id"], "single"),
        ]
    )


def songs_unordered() -> Songs:
    return Songs.create(
        [
            Song("aguacate", "1111", "2021-10-14", ["artist_id"], "single"),
            Song("aguacate", "2222", "2021-10-13", ["artist_id"], "single"),
            Song("aguacate", "3333", "2021-10-10", ["artist_id"], "single"),
            Song("aguacate", "4444", "2021-10-15", ["artist_id"], "single")
        ]
    )


def songs_ordered() -> Songs:
    return Songs.create(
        [
            Song("aguacate", "4444", "2021-10-15", ["artist_id"], "single"),
            Song("aguacate", "1111", "2021-10-14", ["artist_id"], "single"),
            Song("aguacate", "2222", "2021-10-13", ["artist_id"], "single"),
            Song("aguacate", "3333", "2021-10-10", ["artist_id"], "single"),

        ]
    )


def a_song() -> Song:
    return Song(
        "someName",
        "abc1234",
        "",
        ["artist_id"],
        "single"
    )
