import json
import requests
from models.album import Album
from dom_loader import DomLoader

class NickCaveLyricsScraper():
    def __init__(self):
        url = 'https://www.nickcave.com/lyrics'
        self.dom_loader = DomLoader(requests.get(url))
        self.dom = self.dom_loader.dom()

    def create_albums_and_songs(self):
        Album.create_from_dom(self.dom)

    def albums(self):
        return self.dom_loader.capture_albums()

if __name__ == '__main__':
    scraper = NickCaveLyricsScraper()
    albums = scraper.albums()
    albums_index = []
    for album in albums:
        album_id = album['id']
        album_link = {}
        album_link['title'] = album['title']
        album_link['id'] = album['id']
        albums_index.append(album_link)

        with open(f'site/data/albums/{album_id}.json', 'w') as json_file:
            json.dump(album, json_file)

    for album in albums_index:
        with open('site/data/albums/albums.json', 'w') as json_file:
            json.dump(albums_index, json_file)
