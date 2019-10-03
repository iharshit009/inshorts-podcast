import sys
import urllib.request
import bs4 as bs
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import csv


class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()

url = "https://inshorts.com/en/read"
client_response = Client(url)
source = client_response.mainFrame().toHtml()

soup = bs.BeautifulSoup(source, 'lxml')


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
        print("Couldn't not find any link")
