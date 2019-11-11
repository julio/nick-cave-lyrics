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

    def to_hash(self):
        return self.dom_loader.to_hash()

if __name__ == '__main__':
    scraper = NickCaveLyricsScraper()
    albums_dict = scraper.to_hash()
    with open('output/nick-cave-lyrics.json', 'w') as json_file:
        json.dump(albums_dict, json_file)
    # parser.create_albums_and_songs()
