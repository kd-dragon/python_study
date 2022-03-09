from ursina import *


class Background:

    texture_path = '/image/'

    def __init__(self):
        # 배경화면 만들기
        self.background = Entity(
            model='cube',
            texture= Background.texture_path + 'bg.png',  # 배경화면 이미지
            scale=(40, 20, 1),  # 크기 ( x, y ,z )
            z=2  # 땅보다 뒤에 있어야하므로
        )

    def change_texture(self, fname):
        self.background.texture=fname


