import requests
import urllib.request
from bs4 import BeautifulSoup
from models.song import Song

class Album:
    def __init__(self, title, album_songs):
        self.title = title
        self.songs = album_songs

    def record_song_lyrics(self):
        print('==================', self.title, '==================')

        for song_data in self.songs:
            song_title = song_data.contents[0]
            link_to_song_lyrics = song_data['href']
            response_from_song_lyrics_page = requests.get(link_to_song_lyrics)
            song_lyrics_page = BeautifulSoup(response_from_song_lyrics_page.text, 'html.parser')
            title = song_lyrics_page.find_all('h1')[0].contents[0]
            year = song_lyrics_page.find_all('div', {'class': 'date'})[0].contents[0]
            lyrics = song_lyrics_page.find_all('div', {'class': 'lyrics'})[0].find_all('p')
            song = Song(self, title, year, lyrics)
            song.record_lyrics()
