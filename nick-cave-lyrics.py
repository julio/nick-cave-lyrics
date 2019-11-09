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
        self.record_albums(albums)
        return albums

    def record_albums(self, albums):
        for album in albums:
            self.record_album(album)

    def record_album(self, album):
        album_data = album.find_all('h3')
        album_songs = album.find_all('a')
        self.record_song_lyrics(album_data, album_songs)

    def record_song_lyrics(self, album_data, album_songs):
        album_title = album_data[0].contents[0]
        for song_data in album_songs:
            song_title = song_data.contents[0]
            link_to_song_lyrics = song_data['href']
            response_from_song_lyrics_page = requests.get(link_to_song_lyrics)
            song_lyrics_page = BeautifulSoup(response_from_song_lyrics_page.text, 'html.parser')
            title = song_lyrics_page.find_all('h1')[0].contents[0]
            year = song_lyrics_page.find_all('div', {'class': 'date'})[0].contents[0]
            lyrics = song_lyrics_page.find_all('div', {'class': 'lyrics'})[0].find_all('p')
            self.__record_lyrics(album_title, title, year, lyrics)

    def __record_lyrics(self, album_title, song_title, year, lyrics):
        print(album_title, '>', song_title, '>', year)
        for paragraph in lyrics:
            print(paragraph.contents)

if __name__ == '__main__':
    parser = NickCaveLyricsParser()
    parser.record_albums()
