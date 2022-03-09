from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d



class Myplayer:

    texture_path = '/image/'

    def __init__(self):

        self.myplayer = PlatformerController2d(
            position=(-15,-5), 
            texture= Myplayer.texture_path +'mario.png', 
            scale = 1,
            color=color.white,
            max_jumps= 1
        )
    
    def my_setting(self,scale,max_jump):
        self.myplayer.scale = scale
        self.myplayer.max_jumps = max_jump
            