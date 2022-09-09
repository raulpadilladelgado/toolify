from source_code.domain.main.valueobjects.DuplicatedSong import DuplicatedSong
from source_code.domain.main.valueobjects.DuplicatedSongs import DuplicatedSongs


def some_duplicated_songs() -> DuplicatedSongs:
    return DuplicatedSongs(
        [
            DuplicatedSong("como sea", "1234", "date", [3, 4])
        ]
    )
