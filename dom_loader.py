import requests
from bs4 import BeautifulSoup

class DomLoader():
    def __init__(self, response):
        dom_parser = BeautifulSoup(response.text, 'html.parser')
        self.albums_dom = dom_parser.find_all('div', {'class': 'lyric-release-wrap-big'})

    def fix_string(self, str):
        return str.\
            replace('\u2018', '\'').\
            replace('\u2028', '...').\
            replace('\u2019', '\'').\
            replace('\u00a0', '').\
            replace('\u2026', '...').\
            replace('\u2013', '-').\
            replace('\u2014', '-').\
            replace('\u201c', '\"').\
            replace('\u201d', '\"').\
            replace('\u00ea', 'e').\
            replace('\u00e0', 'a').\
            strip()

    def normalize_cover_filename(self, album_name):
        return 'site/data/albums/img/' + album_name.replace('/','-').replace(' ','-').replace('!','-') + '.jpg'

    def capture_cover(self, url, album_name):
        cover_path = self.normalize_cover_filename(album_name)
        with open(cover_path, 'wb') as handle:
            res = requests.get(url, stream=True)
            if not res.ok:
                print(res)
            for block in res.iter_content(1024):
                if not block:
                    break
                handle.write(block)
        return cover_path

    def capture_songs(self, album, songs_dom):
        songs = []
        song_id = '1'

        for song_dom_element in songs_dom:
            song = {}

            song_title = self.fix_string(song_dom_element.contents[0])
            link_to_song_lyrics = song_dom_element['href']
            response_from_song_lyrics_page = requests.get(link_to_song_lyrics)
            song_lyrics_page = BeautifulSoup(response_from_song_lyrics_page.text, 'html.parser')
            year = song_lyrics_page.find_all('div', {'class': 'date'})[0].contents[0]
            album['year'] = year # DRY this (done on each song)
            song['id'] = song_id
            song['title'] = song_title
            song['lyrics'] = []

            lyrics = song_lyrics_page.find_all('div', {'class': 'lyrics'})[0].find_all('p')
            for paragraph in lyrics:
                p = self.fix_string(str(paragraph.get_text(' [...]')))
                song['lyrics'].append(p)

            songs.append(song)
            song_id = str(int(song_id) + 1)

        return songs

    def capture_albums(self):
        albums = []
        album_id = '1'

        for dom_element in self.albums_dom:
            album_title = self.fix_string(dom_element.find_all('h3')[0].contents[0])
            url = dom_element.find('img')['data-src']
            cover_path = self.capture_cover(url, album_title)

            album = {}
            album['id']    = album_id
            album['title'] = album_title
            album['cover'] = cover_path
            album['songs'] = self.capture_songs(album, dom_element.find_all('a'))
            albums.append(album)
            print(album)
            album_id = str(int(album_id) + 1)

        return albums

    def dom(self):
        return self.albums_dom
