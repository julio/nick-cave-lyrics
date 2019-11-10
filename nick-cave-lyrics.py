import requests
from bs4 import BeautifulSoup
from models.album import Album

class NickCaveLyricsScraper():
    def __init__(self):
        url = 'https://www.nickcave.com/lyrics'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.albums_dom = soup.find_all('div', {'class': 'lyric-release-wrap-big'})

    def create_albums_and_songs(self):
        for album_dom_element in self.albums_dom:
            Album.create_from_dom(album_dom_element)

if __name__ == '__main__':
    parser = NickCaveLyricsScraper()
    parser.create_albums_and_songs()
