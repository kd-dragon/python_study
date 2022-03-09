import threading
import time

class Massenger(threading.Thread):
    def run(self):
        for _ in range(100):
            print(threading.currentThread().getName())


x = Massenger(name="나는 1번쓰레드입니다.")
y = Massenger(name="나는 2번쓰레드입니다.")

x.start()
y.start()




