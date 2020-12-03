import psycopg2
import matplotlib.pyplot as plt


def get_data(artist_id):

    HOSTNAME = 'localhost'
    USERNAME = 'postgres'
    PASSWORD = 'postgres'
    DATABASE = 'spotify_data'

    connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    cursor = connection.cursor()

    q = f"SELECT ROUND(AVG(danceability), 3), ROUND(AVG(energy), 3), ROUND(AVG(acousticness), 3), ROUND(AVG(instrumentalness), 3), ROUND(AVG(liveness), 3), ROUND(AVG(valence), 3) FROM track_analysis WHERE artist_id = '{artist_id}'"

    cursor.execute(q)
    data = cursor.fetchall()
    connection.close()
    x_axis_labels = ['danceability', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'valence']
    data = [float(str(d)) for d in data[0]]
    plt.figure('a string')
    plt.bar(x_axis_labels, data)
    plt.title("Hello")
    plt.show()
    return data
