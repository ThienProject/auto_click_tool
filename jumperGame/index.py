import pyautogui as pag
import time

cactus = 'images/cactus.png'
cactus2 = 'images/cactus2.png'
cactus3 = 'images/cactus3.png'
findIsCactus = False
time.sleep(2)
cactusPick = cactus
while not findIsCactus:
    try:
        findIsCactus = pag.locateOnScreen(cactus, confidence=0.9)
        if not findIsCactus:
            findIsCactus = pag.locateOnScreen(cactus2, confidence=0.9)
            cactusPick = cactus2
            if not findIsCactus:
                findIsCactus = pag.locateOnScreen(cactus3, confidence=0.9)
                cactusPick = cactus3
        i = findIsCactus.left
        while findIsCactus:
            print((findIsCactus))
            i =  pag.locateOnScreen(cactusPick, confidence=0.9).left
            print(i)
            if(i <= 776):
                pag.press("up", presses=3)
                print("jump")
                break
        findIsCactus = False
        print("findIsCactus",findIsCactus)
    except pag.ImageNotFoundException:
        pass
print(findIsCactus)

