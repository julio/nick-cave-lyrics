import requests
import urllib.request
import time
from bs4 import BeautifulSoup

class NickCaveLyricsParser():
    def __init__(self):
        url = 'https://www.nickcave.com/lyrics'
        response = requests.get(url)
        self.soup = BeautifulSoup(response.text, 'html.parser')
        self.albums = self.fetch_albums()

    def fetch_albums(self):
        albums = self.soup.find_all('div', {'class': 'lyric-release-wrap-big'})
        self.album_names = []
        for album in albums:
            album_data = album.find_all('h3')
            self.album_names.append(album_data[0].contents[0])

        return albums

    def get_album_names(self):
        return self.album_names

parser = NickCaveLyricsParser()
album_names = parser.get_album_names()
print(album_names)