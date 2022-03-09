import pyautogui
import time

#x=24, y=380
#x=1344, y=201
#pyautogui.moveTo(31, 854, 3)
pyautogui.click(1344, 201)
#time.sleep(3)
#pyautogui.typewrite('Hello World')
#time.sleep(0.5)
#pyautogui.typewrite(['enter', 'space'])
#time.sleep(0.5)
#pyautogui.typewrite('abc')

#pyautogui.screenshot('8.png', region=(1541, 545, 30, 30))


i = pyautogui.locateCenterOnScreen('9.png')

pyautogui.click(i)


