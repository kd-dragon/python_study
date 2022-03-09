class Programmer:

    languages = []                   # 클래스 변수 선언
    language = 'JAVA'

    def __init__(self, name):        # 초기화 함수 재정의
        self.name = name             # 인스턴스 변수 선언 및 초기화

    def add_lang(self, lang):
        self.languages.append(lang)  # 클래스 변수 값 변경경

yong = Programmer('Ray Kim')
yong.add_lang('Python')
yong.add_lang('Java')
print(yong.name)
print(yong.languages)

semi = Programmer('Semi Kim')
print(semi.name)
print(semi.languages) # 무엇이 찍힐까요?