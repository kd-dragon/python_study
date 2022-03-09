import pyautogui, random
import time

#x=24, y=380
#x=1344, y=201
#pyautogui.moveTo(31, 854, 3)
#pyautogui.click(1344, 201)
#time.sleep(3)
#pyautogui.typewrite('Hello World')
#time.sleep(0.5)
#pyautogui.typewrite(['enter', 'space'])
#time.sleep(0.5)
#pyautogui.typewrite('abc')

#pyautogui.screenshot('8.png', region=(1541, 545, 30, 30))

def sendMsg(msg):
    print(msg)
    pyautogui.typewrite(msg)
    pyautogui.typewrite(['enter'])

i = pyautogui.locateCenterOnScreen('offline.png')
j = pyautogui.locateCenterOnScreen('online.png')
print(i)
pyautogui.click(i)
time.sleep(1)
x = random.randrange(1,7)

if i != 'None':
    msg = 'djswpemfdjdhsi zz'
    if x % 2 == 0:
        msg += '.'
    else:
        msg = msg.replace('.', '')
    sendMsg(msg)
elif j != 'None':
    msg = 'rkxdl rr'
    if x % 2 == 0:
        msg += '.'
    else:
        msg = msg.replace('.', '')
    sendMsg(msg)
else:
    print('해당 이미지가 없습니다.')


