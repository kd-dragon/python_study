class BookReader:
    _COUNTRY = 'South Korea'

    def __init__(self, name):
        self.name = name

    def read_book(self):
        print(self.name, 'is reading in', BookReader._COUNTRY)


ray = BookReader('Ray Kim')
semi = BookReader('Semi Kim')

ray.read_book()
semi.read_book()

ray._COUNTRY = 'USA'
ray.read_book()
semi.read_book()