from ursina import *
from itertools import product
from itertools import permutations
from itertools import combinations

import time
import datetime

# system on/off
system_status = 'ON'

class PlayButton:

    def __init__(self, val_x, val_y, num):
        self.next_number = -1
        self.my_number = num
        self.button = Button(
            color=color.random_color(),
            scale=0.2,
            x=val_x,
            y=val_y,
            text=str(self.my_number),
            disabled=False
        )
        self.button.on_click = self.disappear_button

    def disappear_button(self):
        if self.next_number == self.my_number:
            self.button.disabled=True
            self.button.disable()


def time_check():
    return time.time()

app = Ursina()

# 시간 체크용
start_time = time_check()

# 버튼 list
buttons = []

# 숫자 1부터 9 까지 랜덤
ranges = list(range(1, 10))
random.shuffle(ranges)

# -0.2 ~ 0.2 조합 구하기 (x,y 축)
items = [-0.2, 0, 0.2]

pos = list(product(items, repeat=2))

# itertools 모듈: 순열, 조합, 경우의 수 함수 제공
# 조합(combinations): 한 리스트에서 중복을 허용하지 않고 모든 경우의 수를 구하는 것
# 순열(permutations): 한 리스트에서 중복을 허용(순서가 다르면 다른 것이라고 여김)한 경우의 수를 구한다.
# product: 리스트의 모든 경우의 수를 구한다.

print(pos)

for idx, val in enumerate(ranges):
    buttons.append(PlayButton(pos[idx][0], pos[idx][1], val))

# 윈도우 창 경계 생성
window.borderless = False

# 윈도우 창 색 설정
window.color = color.light_gray

# 폰트 설정
Text.default_font='./font/NanumGothicCodingBold.ttf'



def update():
    global start_time
    global system_status

    global buttons

    min_number = 0
    active_buttons = [btn for btn in buttons if btn.button.disabled == False]

    # 버튼 다 없앴을 때
    if(len(active_buttons) == 0 and system_status == 'ON'):
        time_cost = time.time() - start_time
        print(datetime.timedelta(seconds=time_cost))

        # datetime: 날짜/시간을 처리하는 모듈
        datetimes = str(datetime.timedelta(seconds=time_cost)).split(".")
        print(datetimes)
        datetimes = datetimes[0]

        Button(
            color=color.random_color(),
            scale=0.5,
            x=0,
            y=0,
            text="소요시간:[{}]".format(datetimes),
            disabled=False
        )
        system_status = 'OFF'
    else:
        for idx, obj in enumerate(active_buttons):
            if idx == 0:
                min_number = obj.my_number
            else :
                if min_number > obj.my_number:
                    min_number = obj.my_number

        for button in active_buttons:
            button.next_number = min_number



app.run()
