import requests

with open('website-urls.txt') as url_data:
    urls = url_data.readlines()
    for url in urls:
        page = requests.get(url)
        