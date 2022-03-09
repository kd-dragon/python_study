from ursina import *

app = Ursina()

# 윈도우 창 경계 생성
window.borderless = False

# 윈도우 창 색 설정
window.color = color.light_gray

# 폰트 설정
Text.default_font='./font/NanumGothicCodingBold.ttf'

number = random.randint(1, 20)

button1 = Button(
            color=color.random_color(),
            scale=0.2,
            text=str(number)
        )

button2 = Button(
            color=color.random_color(),
            scale=0.2,
            x=0.2,
            text="초기화"
        )


def number_increase():
    global number
    number += 1
    # button1.text = str(number)


def number_decrease():
    global number

    if number <= 1:
        button1.disable() # remove, disable, none, delete, drop...
    else:
        number -= 1
        # button1.text = str(number)


def initialize():
    global number
    number = 0
    # button1.text = str(number)


button1.on_click = number_decrease
button2.on_click = initialize


def update():
    global number
    button1.text = str(number)
    # print(button1.text)

# 마우스 클릭으로 블럭 없애기 !


app.run()