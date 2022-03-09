class BookReader:
    country = 'South Korea' # 클래스 변수

    def __init__(self, name):
        self.name = name

    def read_book(self):
        print(self.name, 'is reading in', self.country)


ray = BookReader('Ray Kim')
print(BookReader.country)
ray.country = 'U.S.A'
ray.read_book()

semi = BookReader('Semi Kim')
semi.read_book()


