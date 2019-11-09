import requests
import sqlalchemy
import urllib.request
import time
from bs4 import BeautifulSoup

class Album:
    def __init__(self, title, album_songs):
        self.title = title
        self.songs = album_songs

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
        self.record_song_lyrics(album)

    def record_song_lyrics(self, album):
        for song_data in album.songs:
            song_title = song_data.contents[0]
            link_to_song_lyrics = song_data['href']
            response_from_song_lyrics_page = requests.get(link_to_song_lyrics)
            song_lyrics_page = BeautifulSoup(response_from_song_lyrics_page.text, 'html.parser')
            title = song_lyrics_page.find_all('h1')[0].contents[0]
            year = song_lyrics_page.find_all('div', {'class': 'date'})[0].contents[0]
            lyrics = song_lyrics_page.find_all('div', {'class': 'lyrics'})[0].find_all('p')
            self.__record_lyrics(album.title, title, year, lyrics)

    def __record_lyrics(self, album_title, song_title, year, lyrics):
        print(album_title, '>', song_title, '>', year)
        for paragraph in lyrics:
            print(paragraph.contents)

if __name__ == '__main__':
    parser = NickCaveLyricsScraper()
