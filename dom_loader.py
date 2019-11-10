from bs4 import BeautifulSoup

class DomLoader():
    def __init__(self, response):
        dom_parser = BeautifulSoup(response.text, 'html.parser')
        self.albums_dom = dom_parser.find_all('div', {'class': 'lyric-release-wrap-big'})

    def dom(self):
        return self.albums_dom
