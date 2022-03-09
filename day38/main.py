from fake_mario import *
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

if __name__ == '__main__':
    print("내가 바로 시작점이다")

# 3D 기본 모델
app = Ursina()

# 2D 게임 만들때 중요한 것
camera.orthographic = True
camera.fov = 20   # field of view : 화면에 얼마나 넓게 보일 것인가

background = Background()
ground = Ground()
background.change_texture("sonic.png")

app.run()