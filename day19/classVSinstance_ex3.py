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
# semi.read_book()   # 어떻게 나올 것인가?

# 올바른 클래스 변수 접근 방법은 무엇일까?

