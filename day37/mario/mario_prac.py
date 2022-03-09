from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

# 3D 기본 모델 / 2D 지원 Ok
app = Ursina()

# 2D 게임 만들 때 중요한 설정
camera.orthographic=True
camera.fov=20 # Field of view 화면에 얼마나 넓게 보일 것인가

# Entity: 우르시나의 기본 객체, 모든 것을 만들 수 있는 기초 재료
ground = Entity(
    model='cube', #정육면체
    color=color.rgb(50,180,50),
    z=0.1,
    y=-8,
    scale=(100, 5, 10), # 크기
    collider='box' # 충돌 판정에 중요한 옵션
)

# 배경화면 설정
background = Entity(
    model='cube',
    texture='bg.png', # 배경화면 이미지
    scale=(40, 20, 1), # 크기 (x, y, z)
    z=2 # 땅보다 뒤에 있어야 하므로..
)


# 플레이어 - 우르시나 기본 제공하는 PlatformerController2d 사용
player = PlatformerController2d(
    position=(-15, -5),  # 시작 위치 조절 가능
    texture='mario.png',  # 플레이어 꾸미기
    scale=1,
    color=color.white,
    max_jumps=2  # 2단 점프 구현
)

# 발판 만들기

for w in range(2):
    wall = Entity(
        model='cube',
        color=color.rgb(111, 79, 40),
        collider='box',
        scale=(1, 1),
        position=(random.randint(-10, 10), -2)
    )


# 장애물 만들기
spikes = []

for i in range(10):
    spike = Entity(
        model='cube',
        texture='spike.png',
        color=color.white,  #  거의 투명한 색
        collider='box',
        #position=(5,-5),
        position=(random.randint(-10, 10), -5),
        scale=1
    )
    spikes.append(spike)


def update():
    hit_info = player.intersects() #플레이어가 겹치는 이벤트가 발생할때 받아오는 정보
    # 부딪히면 True 반환
    if hit_info.hit:
        if hit_info.entity in spikes:  # 만약 해당 엔티티가 spikes 중 하나라면
            player.position = (-15, -5)  # 원점으로 돌아가기

app.run()