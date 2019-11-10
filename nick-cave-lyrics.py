import requests
from bs4 import BeautifulSoup
from models.album import Album

class NickCaveLyricsScraper():
    def __init__(self):
        url = 'https://www.nickcave.com/lyrics'
        self.fetch_albums(url)

    def fetch_albums(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        albums = soup.find_all('div', {'class': 'lyric-release-wrap-big'})
        self.record_albums(albums)

    def record_albums(self, albums):
        for album in albums:
            self.record_album(album)

    def record_album(self, album_page):
        album_data = album_page.find_all('h3')
        title = album_data[0].contents[0]

        album_songs = album_page.find_all('a')

        album = Album(title, album_songs)
        album.record_song_lyrics()

if __name__ == '__main__':
    parser = NickCaveLyricsScraper()
