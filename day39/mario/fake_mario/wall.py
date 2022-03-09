from ursina import *

class Wall:

    def __init__(self):

        for i in range(3):
            self.wall = Entity(
                model='cube',
                color=color.rgb(111,79,40),
                collider='box',
                position=(random.randint(-10,10),-2),
                scale=(2,1)   
            )