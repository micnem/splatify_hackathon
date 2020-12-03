import psycopg2


def commit_db(features, artist_id):

    HOSTNAME = 'localhost'
    USERNAME = 'postgres'
    PASSWORD = 'postgres'
    DATABASE = 'spotify_data'

    connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    cursor = connection.cursor()

    

    for track_dict in features:
        track_dict = {"track_id" if k == 'id' else k:v for k,v in track_dict.items()}
        track_dict['artist_id'] = artist_id
        q = "INSERT INTO track_analysis (danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, type, track_id, uri, track_href, analysis_url, duration_ms, time_signature, artist_id) VALUES(%(danceability)s, %(energy)s, %(key)s, %(loudness)s, %(mode)s, %(speechiness)s, %(acousticness)s, %(instrumentalness)s, %(liveness)s, %(valence)s, %(tempo)s, %(type)s, %(track_id)s, %(uri)s, %(track_href)s, %(analysis_url)s, %(duration_ms)s, %(time_signature)s, %(artist_id)s)"

        cursor.execute(q, track_dict)
        connection.commit() 

    connection.close()

def add_artist(artist_name):

    HOSTNAME = 'localhost'
    USERNAME = 'postgres'
    PASSWORD = 'postgres'
    DATABASE = 'spotify_data'

    connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    cursor = connection.cursor()
    
    q = f"INSERT INTO artist (artist_name) VALUES('{artist_name}')"

    cursor.execute(q)
    connection.commit()
    connection.close()

def check_artist(artist_name):
    HOSTNAME = 'localhost'
    USERNAME = 'postgres'
    PASSWORD = 'postgres'
    DATABASE = 'spotify_data'

    connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    cursor = connection.cursor()
    
    q = f"SELECT id FROM artist WHERE artist_name = '{artist_name}'"

    cursor.execute(q)
    artist_id = cursor.fetchone()
    connection.close()
    return artist_id
