from unittest import TestCase

from source_code.domain.main.value_objects.Song import Song
from source_code.application.main.services.FindDuplicatedSong import find_duplicated_song


class FindDuplicatedSongTest(TestCase):
    def test_find_duplicated_song(self):
        given_songs = a_given_songs()

        actual_result = find_duplicated_song(given_songs)

        expected_result = list()
        expected_result.append(Song('hello world', '1234'))
        self.assertEqual(str(expected_result.pop(0)), str(actual_result.pop(0)))


REPEATED_NAME = 'hello world'


def a_given_songs():
    return [
        {
            'track': {
                'id': '1234',
                'name': REPEATED_NAME
            }
        },
        {
            'track': {
                'album': {
                    'release_date': '2021-10-10'
                },
                'id': '1234',
                'name': REPEATED_NAME
            }
        },
        {
            'track': {
                'id': '1234',
                'name': 'hello world vol 2'
            }
        }
    ]
