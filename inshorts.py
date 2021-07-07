#import Harshit jain
import sys
import urllib.request
import bs4 as bs
import csv
import requests

url = "https://inshorts.com/en/read"
source = requests.get(url)

soup = bs.BeautifulSoup(source.content, 'html.parser')


for require in soup.find_all('div', class_='news-card z-depth-1'):
    headlines = require.find('span', attrs={'itemprop': 'headline'}).text
    print(headlines)

    authors = require.find('span', attrs={'class': 'author'}).text
    print(authors)

    time = require.find('span', attrs={'class': 'time'}).text
    print(time)

    dates = require.find('span', attrs={'class': 'date'}).text
    print(dates)

    content = require.find('div', itemprop='articleBody').text
    print(content)

    try:
        href_tags = require.find('a', attrs={'href': re.compile("^http://")})
        print(href_tags.get('href'))
    except:

        print("**********Couldn't not find any link************")
