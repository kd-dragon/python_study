from ursina import *


class PlayButton:

    def __init__(self, val_x):
        self.number = random.randint(1, 20)
        self.button = Button(
            color=color.random_color(),
            scale=0.2,
            x=val_x,
            text=str(self.number)
        )

        self.button.on_click = self.number_decrease

    def number_decrease(self):
        if self.number <= 1:
            self.button.disable()  # remove, disable, none, delete, drop...
        else:
            self.number -= 1
            self.button.text = str(self.number)


app = Ursina()

# 윈도우 창 경계 생성
window.borderless = False

# 윈도우 창 색 설정
window.color = color.light_gray

# 폰트 설정
Text.default_font='./font/NanumGothicCodingBold.ttf'

button1 = PlayButton(0.2)
button2 = PlayButton(0)

app.run()