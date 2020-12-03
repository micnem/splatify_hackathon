import track_features as tf
from to_db import commit_db, add_artist, check_artist
import graph_gen

artist_name = input('Input artist name: ')

# If artist not in artist table, update
artist_id = check_artist(artist_name)
if artist_id == None:
    add_artist(artist_name)
    artist_id = check_artist(artist_name)[0]
    track_info_list = tf.find_features(artist_name)

    commit_db(track_info_list, artist_id)
else:
    track_info_list = tf.find_features(artist_name)

    commit_db(track_info_list, artist_id[0])

graph_gen.get_data(artist_id[0])



