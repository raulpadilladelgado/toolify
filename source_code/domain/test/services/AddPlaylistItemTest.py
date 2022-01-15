import unittest

from source_code.domain.main.services.AddPlaylistItems import split_songs_list_by_chunks

FAKE_SONG_ID_ONE = 'SONG_ID_Z'


class AddPlaylistItemsTest(unittest.TestCase):

    def test_split_songs_list_by_chunks(self):
        songs_list = []
        for _ in range(10):
            songs_list.append(FAKE_SONG_ID_ONE)

        splited_song_list = split_songs_list_by_chunks(songs_list, 2)

        expected_result = [
            [FAKE_SONG_ID_ONE, FAKE_SONG_ID_ONE],
            [FAKE_SONG_ID_ONE, FAKE_SONG_ID_ONE],
            [FAKE_SONG_ID_ONE, FAKE_SONG_ID_ONE],
            [FAKE_SONG_ID_ONE, FAKE_SONG_ID_ONE],
            [FAKE_SONG_ID_ONE, FAKE_SONG_ID_ONE]
        ]
        self.assertEqual(expected_result, splited_song_list)
