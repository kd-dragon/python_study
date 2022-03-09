import pyautogui as auto





def zyra_ban():

    play = auto.locateCenterOnScreen('play.png')
    on = auto.locateCenterOnScreen('on.png')
    off = auto.locateCenterOnScreen('off.png')
    
    

    if play:

        auto.moveTo(play)
        auto.doubleClick()

        auto.write('support gap')
        auto.press('enter')


    elif on:

        auto.moveTo(on)
        auto.doubleClick()

        auto.write('support gap')
        auto.press('enter')

    elif off:

        auto.moveTo(off)
        auto.doubleClick()


        auto.write('support gap')
        auto.press('enter')


zyra_ban()







