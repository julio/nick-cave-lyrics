class Song:
    def __init__(self, album, title, year, lyrics):
        self.title = title
        self.album = album
        self.year = year
        self.lyrics = lyrics

    def record_lyrics(self):
        print('---', self.title, '-', self.year, '---')
        for paragraph in self.lyrics:
            print(paragraph.contents)
