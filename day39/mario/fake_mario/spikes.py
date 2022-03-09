from ursina import *


class Spikes:

    spikes = []

    def __init__ (self):

        
        for i in range(10):
            self.spike = Entity(
                model='cube',
                texture='spike.png',
                color=color.white, # 거의 투명한 색
                collider='box',
                position=(random.randint(-10,10),-5),
                scale=(1,1)
            )
            Spikes.spikes.append(self.spike)