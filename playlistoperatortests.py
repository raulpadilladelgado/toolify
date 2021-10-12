import unittest
from playlistoperator import PlaylistOperator
from unittest.mock import Mock
import spotipy


class MyTestCase(unittest.TestCase):

    def test_show_playlists(self):
        spotipy_mock_returned_value = {
            'href': 'https://api.spotify.com/v1/users/11172067860/playlists?offset=0&limit=1', 'items': [
                {'collaborative': False,
                 'description': 'Your weekly mixtape of fresh music. Enjoy new music and deep cuts picked for you. Updates every Monday.',
                 'external_urls': {'spotify': 'https://open.spotify.com/playlist/37i9dQZEVXcWTsLEWE5BJV'},
                 'href': 'https://api.spotify.com/v1/playlists/37i9dQZEVXcWTsLEWE5BJV', 'id': '37i9dQZEVXcWTsLEWE5BJV',
                 'images': [{'height': None,
                             'url': 'https://newjams-images.scdn.co/image/ab676477000033ad/dt/v3/discover-weekly/aAbca4VNfzWuUCQ_FGiEFA==/bmVuZW5lbmVuZW5lbmVuZQ==',
                             'width': None}], 'name': 'Discover Weekly', 'owner': {'display_name': 'Spotify',
                                                                                   'external_urls': {
                                                                                       'spotify': 'https://open.spotify.com/user/spotify'},
                                                                                   'href': 'https://api.spotify.com/v1/users/spotify',
                                                                                   'id': 'spotify', 'type': 'user',
                                                                                   'uri': 'spotify:user:spotify'},
                 'primary_color': None, 'public': False,
                 'snapshot_id': 'MCwwMDAwMDAwMDg0MzVlZGQ0YzI2ZDZjMDliZWE2ZWY1ZDE5NDg2N2Qw',
                 'tracks': {'href': 'https://api.spotify.com/v1/playlists/37i9dQZEVXcWTsLEWE5BJV/tracks', 'total': 30},
                 'type': 'playlist', 'uri': 'spotify:playlist:37i9dQZEVXcWTsLEWE5BJV'}], 'limit': 1,
            'next': 'https://api.spotify.com/v1/users/11172067860/playlists?offset=1&limit=1', 'offset': 0,
            'previous': None, 'total': 10}
        spotipy_mock = spotipy
        spotipy_mock.current_user_playlists = Mock(return_value=spotipy_mock_returned_value)
        playlist_operator = PlaylistOperator(spotipy_mock)

        user_playlists = playlist_operator.list_user_playlists()

        expected_result = 'Discover Weekly - 37i9dQZEVXcWTsLEWE5BJV\n'
        self.assertEqual(user_playlists, expected_result)

    def test_reorder_playlists(self):
        spotipy_mock_returned_value = {
            'items': [{'added_at': '2021-10-03T08:44:59Z', 'added_by': {
                'external_urls': {'spotify': 'https://open.spotify.com/user/11172067860'},
                'href': 'https://api.spotify.com/v1/users/11172067860', 'id': '11172067860', 'type': 'user',
                'uri': 'spotify:user:11172067860'}, 'is_local': False, 'primary_color': None, 'track': {
                'album': {'album_type': 'single', 'artists': [
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/329e4yvIujISKGKz1BZZbO'},
                     'href': 'https://api.spotify.com/v1/artists/329e4yvIujISKGKz1BZZbO',
                     'id': '329e4yvIujISKGKz1BZZbO',
                     'name': 'Farruko', 'type': 'artist', 'uri': 'spotify:artist:329e4yvIujISKGKz1BZZbO'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/00CMSJdbf36zOzKB3z8JrR'},
                     'href': 'https://api.spotify.com/v1/artists/00CMSJdbf36zOzKB3z8JrR',
                     'id': '00CMSJdbf36zOzKB3z8JrR',
                     'name': 'Victor Cardenas', 'type': 'artist', 'uri': 'spotify:artist:00CMSJdbf36zOzKB3z8JrR'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/3JfbHWZ07sSBjbojTU2hAt'},
                     'href': 'https://api.spotify.com/v1/artists/3JfbHWZ07sSBjbojTU2hAt',
                     'id': '3JfbHWZ07sSBjbojTU2hAt',
                     'name': 'Dj Adoni', 'type': 'artist', 'uri': 'spotify:artist:3JfbHWZ07sSBjbojTU2hAt'}],
                          'available_markets': ['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB',
                                                'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BT',
                                                'BW', 'BY', 'BZ', 'CA', 'CH', 'CI', 'CL', 'CM', 'CO', 'CR', 'CV', 'CW',
                                                'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES',
                                                'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD', 'GE', 'GH', 'GM', 'GN', 'GQ',
                                                'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL',
                                                'IN', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN',
                                                'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU',
                                                'LV', 'MA', 'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MN', 'MO', 'MR',
                                                'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL',
                                                'NO', 'NP', 'NR', 'NZ', 'OM', 'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PS',
                                                'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SE',
                                                'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SR', 'ST', 'SV', 'SZ', 'TD', 'TG',
                                                'TH', 'TL', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US',
                                                'UY', 'UZ', 'VC', 'VN', 'VU', 'WS', 'XK', 'ZA', 'ZM', 'ZW'],
                          'external_urls': {'spotify': 'https://open.spotify.com/album/046Eyq94B09gkJ8ISXxzt8'},
                          'href': 'https://api.spotify.com/v1/albums/046Eyq94B09gkJ8ISXxzt8',
                          'id': '046Eyq94B09gkJ8ISXxzt8', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2733ca3e2c3dc898f52caa43ca0',
                         'width': 640},
                        {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e023ca3e2c3dc898f52caa43ca0',
                         'width': 300},
                        {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048513ca3e2c3dc898f52caa43ca0',
                         'width': 64}], 'name': 'El Incomprendido', 'release_date': '2021-09-30',
                          'release_date_precision': 'day', 'total_tracks': 1, 'type': 'album',
                          'uri': 'spotify:album:046Eyq94B09gkJ8ISXxzt8'}, 'artists': [
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/329e4yvIujISKGKz1BZZbO'},
                     'href': 'https://api.spotify.com/v1/artists/329e4yvIujISKGKz1BZZbO',
                     'id': '329e4yvIujISKGKz1BZZbO',
                     'name': 'Farruko', 'type': 'artist', 'uri': 'spotify:artist:329e4yvIujISKGKz1BZZbO'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/00CMSJdbf36zOzKB3z8JrR'},
                     'href': 'https://api.spotify.com/v1/artists/00CMSJdbf36zOzKB3z8JrR',
                     'id': '00CMSJdbf36zOzKB3z8JrR',
                     'name': 'Victor Cardenas', 'type': 'artist', 'uri': 'spotify:artist:00CMSJdbf36zOzKB3z8JrR'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/3JfbHWZ07sSBjbojTU2hAt'},
                     'href': 'https://api.spotify.com/v1/artists/3JfbHWZ07sSBjbojTU2hAt',
                     'id': '3JfbHWZ07sSBjbojTU2hAt',
                     'name': 'Dj Adoni', 'type': 'artist', 'uri': 'spotify:artist:3JfbHWZ07sSBjbojTU2hAt'}],
                'available_markets': ['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD',
                                      'BE',
                                      'BF', 'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ',
                                      'CA',
                                      'CH', 'CI', 'CL', 'CM', 'CO', 'CR', 'CV', 'CW', 'CY', 'CZ', 'DE', 'DJ', 'DK',
                                      'DM',
                                      'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD',
                                      'GE',
                                      'GH', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU',
                                      'ID',
                                      'IE', 'IL', 'IN', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM',
                                      'KN',
                                      'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV',
                                      'MA',
                                      'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MN', 'MO', 'MR', 'MT', 'MU', 'MV',
                                      'MW',
                                      'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM',
                                      'PA',
                                      'PE', 'PG', 'PH', 'PK', 'PL', 'PS', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RU',
                                      'RW',
                                      'SA', 'SB', 'SC', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SR', 'ST', 'SV',
                                      'SZ',
                                      'TD', 'TG', 'TH', 'TL', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG',
                                      'US',
                                      'UY', 'UZ', 'VC', 'VN', 'VU', 'WS', 'XK', 'ZA', 'ZM', 'ZW'], 'disc_number': 1,
                'duration_ms': 267546, 'episode': False, 'explicit': True, 'external_ids': {'isrc': 'USSD12100701'},
                'external_urls': {'spotify': 'https://open.spotify.com/track/493Rk3iS7rs8uPfpnfm95u'},
                'href': 'https://api.spotify.com/v1/tracks/493Rk3iS7rs8uPfpnfm95u', 'id': '493Rk3iS7rs8uPfpnfm95u',
                'is_local': False, 'name': 'El Incomprendido', 'popularity': 75,
                'preview_url': 'https://p.scdn.co/mp3-preview/1e86dfa0b9940ac5e43ae90285f8259c7b44a8d5?cid=a8ea86f942ba45f1b78d235cd20e90b5',
                'track': True, 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:493Rk3iS7rs8uPfpnfm95u'},
                       'video_thumbnail': {'url': None}}]}
        spotipy_mock = spotipy
        spotipy_mock.playlist_items = Mock(return_value=spotipy_mock_returned_value)
        playlist_operator = PlaylistOperator(spotipy_mock)

        user_playlists = playlist_operator.reorder_playlist('Playlist ID')

        expected_result = {'493Rk3iS7rs8uPfpnfm95u': '2021-09-30'}
        self.assertEqual(user_playlists, expected_result)
