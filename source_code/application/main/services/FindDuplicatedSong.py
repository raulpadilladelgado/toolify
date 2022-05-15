from source_code.domain.main.valueobjects.Song import Song


def find_duplicated_song(songs) -> list:
    not_duplicated_songs = list()
    duplicated_songs = list()
    for song in songs:
        if song['track']['name'] in not_duplicated_songs:
            duplicated_songs.append(Song(song['track']['name'], song['track']['id']))
        else:
            not_duplicated_songs.append(song['track']['name'])
    return duplicated_songs if len(duplicated_songs) > 0 else []
