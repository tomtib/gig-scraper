from ast import pattern
import requests
import re



with open('website-urls.txt') as url_data:
    urls = url_data.readlines()
    for url in urls:
        print(url)
        list_of_dates = []
        page_data = requests.get(url)
        page_str = page_data.text
        page = page_str.split()
        pattern = re.compile(r"(?=[^A-Za-z0-9]event[^A-Za-z0-9])(.*)")
        for match in pattern.finditer(page):
            date = re.search("\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", match.group(2))
            if date:
                print(date)
                if date.group(0) not in list_of_dates:
                    list_of_dates.append(date)
        print(list_of_dates)