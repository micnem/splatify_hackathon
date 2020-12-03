from __future__ import print_function   
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
pp = pprint.PrettyPrinter(indent=4)

def find_features(artist_name):

    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace = False



    results = sp.search(q=artist_name, limit=10)

    tids = []
    for i, t in enumerate(results['tracks']['items']):
        # print(' ', i, t['name'])
        tids.append(t['uri'])

    features = sp.audio_features(tids)
    return features
 
