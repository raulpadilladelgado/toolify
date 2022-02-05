from source_code.domain.main.value_objects.Playlist import Playlist


def transform_items_to_playlists(results, user_id):
    final_result = []
    for ixd, item in enumerate(results['items']):
        if item['owner']['id'] == user_id:
            final_result.append(Playlist(
                item['name'],
                item['id'],
                item['description'],
                item['images'][0]['url'],
                item['tracks']['total']
            ))
    return final_result
