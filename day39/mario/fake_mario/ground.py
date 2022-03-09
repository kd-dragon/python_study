from ursina import *


class Ground:

    def __init__(self):
        self.ground = Entity(
            model='cube',  # 정육면체
            color=color.rgb(50, 180, 50),
            z=0.1,
            y=-8,
            scale=(100, 5, 10),  # 크기
            collider='box'  # 충돌 판정에 중요한 옵션
        )

    def change_color_rgb(self, r, g, b):
        self.ground.color = color.rgb(r, g, b)

    def my_setting(self):
        self.ground.color = color.rgb(100, 40, 500)
        self.ground.z=0.2
        self.ground.y=-10
        self.ground.scale=(100, 10, 10)