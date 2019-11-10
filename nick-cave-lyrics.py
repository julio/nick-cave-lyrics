import requests
from models.album import Album
from dom_loader import DomLoader

class NickCaveLyricsScraper():
    def __init__(self):
        url = 'https://www.nickcave.com/lyrics'
        dom_loader = DomLoader(requests.get(url))
        self.dom = dom_loader.dom()

    def create_albums_and_songs(self):
        Album.create_from_dom(self.dom)

if __name__ == '__main__':
    parser = NickCaveLyricsScraper()
    parser.create_albums_and_songs()
