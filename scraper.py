import requests
import re
import json
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

client_id="49e1ae4924774066a717ec7f3cf229d8"
client_secret=os.environ.get("CLIENT_SECRET")
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_website_tracks():
    match_list = []
    url = website.get("url")
    method = website.get("method")
    print("\n" + url + "\n")
    page_data = requests.get(url)
    page_str = page_data.text
    soup = BeautifulSoup(page_str, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if len(match_list) > 5:
            return match_list
        if not href is None:
            if method == 1:
                match_list = method_1(href, match_list)
            if method == 2:
                if re.search("[^A-Za-z0-9](event|events)[^A-Za-z0-9][a-z|\-]*$", href):
                    if href not in match_list:
                        print(href)
                        match_list.append(href)

def method_1(href, match_list):
    if re.search("\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", href):
        artist_name = re.search("\d-(([a-z]|-)*)(-the)", href)
        if artist_name:
            artist_name = artist_name.group(1).replace('-',' ')
            print(artist_name)
            match_list.append(artist_name)
        else:
            print("WARNING: FILTERED_HREF_NOT_CONVERTED_TO_ARTIST; NONETYPE")
    return match_list

def get_artist_uri(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        print(artist['name'], artist['images'][0]['url'])

if __name__=="__main__":
    with open('website-urls.json') as website_data:
        websites = json.load(website_data)
        for website in websites: 
            get_website_tracks()