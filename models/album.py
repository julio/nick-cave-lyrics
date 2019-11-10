import requests
import urllib.request
from bs4 import BeautifulSoup
from models.song import Song

class Album:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def create_from_dom(dom):
        for dom_element in dom:
            album_title = dom_element.find_all('h3')[0].contents[0]
            album = Album(album_title)
            album.save()

            album.add_songs_from_dom(dom_element.find_all('a'))

    def add_songs_from_dom(self, songs_dom):
        for song_dom_element in songs_dom:
            song_title = song_dom_element.contents[0]
            link_to_song_lyrics = song_dom_element['href']
            response_from_song_lyrics_page = requests.get(link_to_song_lyrics)
            song_lyrics_page = BeautifulSoup(response_from_song_lyrics_page.text, 'html.parser')
            title = song_lyrics_page.find_all('h1')[0].contents[0]
            year = song_lyrics_page.find_all('div', {'class': 'date'})[0].contents[0]
            lyrics = song_lyrics_page.find_all('div', {'class': 'lyrics'})[0].find_all('p')
            song = Song(self, title, year, lyrics)
            song.record_lyrics()

    def save(self):
        print('Album:', self.title)
