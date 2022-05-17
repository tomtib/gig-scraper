import requests
import re
import json
from bs4 import BeautifulSoup

with open('website-urls.json') as website_data:
    websites = json.load(website_data)
    for website in websites:
        url = website.get("url")
        method = website.get("method")
        print("\n" + url + "\n")
        page_data = requests.get(url)
        page_str = page_data.text
        soup = BeautifulSoup(page_str, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if not href is None:
                if method == 1:
                    if re.search("\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", href):
                        print(href)
                if method == 2:
                    print(href)
        
        
        
        