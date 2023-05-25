import json
from collections import defaultdict
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def get_my_top_artists(range: str = 'medium_term') -> dict:
    """Get my top artists from Spotify API and return a result dict. 

    Args:
        ranges (list[str], optional): Time range for getting my top artists. Can choose from 'short_term', 'medium_term', 'long_term'. Defaults to ['short_term'].
    
    Returns:
        dict: API response.
    """
    print(f'processing {range} top artists...')
    results = sp.current_user_top_artists(time_range=range, limit=20)
    results = results['items']
    return results


def get_my_top_tracks(range: str = 'medium_term') -> dict:    
    """Extract my top artists from Spotify and return a dataframe. 

    Args:
        ranges (list[str], optional): Time range for getting my top artists. Can choose from 'short_term', 'medium_term', 'long_term'. Defaults to ['short_term'].
    
    Returns:
        dict: API response.
    """
    print(f'processing {range} top tracks...')
    results = sp.current_user_top_tracks(time_range=range, limit=20)
    results = results['items']
    return results


def extract_top_artist_to_df(results: dict[list]) -> pd.DataFrame:
    """Extract top artists infomations from API response and return a Pandas dataframe.

    Args:
        results (dict[list]): API response.

    Returns:
        pd.DataFrame: Top artists informations.
    """
    info_list = []
    for artist in results:
        info_dict = defaultdict()
        info_dict['artist_id'] = artist['id']
        info_dict['artist_name'] = artist['name']
        info_dict['artist_popularity'] = artist['popularity']
        info_dict['genres'] = artist['genres']
        info_dict['artist_url'] = artist['external_urls']['spotify']
        info_dict['image_url'] = artist['images'][0]['url']
        info_list.append(info_dict)
    df = pd.DataFrame.from_dict(info_list)
    return df


def extract_top_track_to_df(results: dict[list]) -> pd.DataFrame:
    """Extract top tracks infomations from API response and return a Pandas dataframe.

    Args:
        results (dict[list]): API response.

    Returns:
        pd.DataFrame: Top artists informations.
    """
    info_list = []
    for track in results:
        info_dict = defaultdict()
        info_dict['track_id'] = track['id']
        info_dict['track_name'] = track['name']
        info_dict['track_popularity'] = track['popularity']
        info_dict['duration_ms'] = track['duration_ms']
        info_dict['track_url'] = track['external_urls']['spotify']
        info_dict['album_name'] = track['album']['name']
        info_dict['album_release_date'] = track['album']['release_date']
        info_dict['artists_name'] = [artist['name'] for artist in track['artists']]
        info_dict['album_image_url'] = track['album']['images'][0]['url']
        info_dict['preview_url'] = track['preview_url']
        info_list.append(info_dict)
    df = pd.DataFrame.from_dict(info_list)
    return df


results = get_my_top_artists()
df = extract_top_artist_to_df(results)
df.to_csv('data/03_primary/my_top_artists.csv')

results = get_my_top_tracks()
df = extract_top_track_to_df(results)
df.to_csv('data/03_primary/my_top_tracks.csv')
