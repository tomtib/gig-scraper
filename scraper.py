import requests
import re
import json
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

scope = "playlist-modify-public"
user_id = "11154880367"

#Authorization Code Flow
os.environ["SPOTIPY_CLIENT_ID"] = "49e1ae4924774066a717ec7f3cf229d8"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8080"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
playlists = sp.user_playlists(user_id)
print(f"\nConfiguring playlist: {playlists['items'][0]['name']}")
playlist_id = playlists['items'][0]['id']

def get_website_tracks():
    match_list = []
    number_added = 0
    url = website.get("url")
    method = website.get("method")
    print("\n" + url + "\n")
    page_data = requests.get(url)
    page_str = page_data.text
    soup = BeautifulSoup(page_str, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if number_added > 3:
            print(f"SUCCESS: HIT {number_added} TRACKS FOR VENUE")
            return 
        if href:
            if method == 1:
                if method_1(href):
                    number_added = number_added + 1
            if method == 2:
                if re.search("[^A-Za-z0-9](event|events)[^A-Za-z0-9][a-z|\-]*$", href):
                    if href not in match_list:
                        print(href)
                        match_list.append(href)
    return

def method_1(href):
    if re.search("\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", href):
        artist_name = re.search("\d-(([a-z]|-)*)(-the)", href)
        if artist_name:
            artist_name = artist_name.group(1).replace('-',' ')
            if get_artist_uri(artist_name):
                return 1
        else:
            print("WARNING: FILTERED_HREF_NOT_CONVERTED_TO_ARTIST; NONETYPE")
    return 0

def get_artist_uri(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if items:
        artist = items[0]
        add_top_song(artist)
        return 1
    return 0

def add_top_song(artist):
    top_tracks = sp.artist_top_tracks(artist['uri'])
    top_track = top_tracks['tracks'][0]['uri']
    print(f"{artist['name']} - {top_track}")
    top_track_uri = [f"{top_track}"]
    sp.playlist_add_items(playlist_id, top_track_uri)
    return

if __name__=="__main__":
    playlist_items = sp.playlist_items(playlist_id)
    item_id_list = []
    for item in playlist_items['items'][1:]:
        item_id_list.append(item['track']['id'])
    sp.playlist_remove_all_occurrences_of_items(playlist_id, item_id_list)
    with open('website-urls.json') as website_data:
        websites = json.load(website_data)
        for website in websites: 
            get_website_tracks()