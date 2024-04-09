import pyautogui as pag
import time

zaloImage = "images/zalo.png"
zaloLocation = pag.locateOnScreen(zaloImage, confidence=0.9)
print("location", zaloLocation)
pag.click(zaloLocation)
time.sleep(1)
coordinatesConversationX = 121
coordinatesConversationY = 143

pag.click(coordinatesConversationX, coordinatesConversationY )

for i in range(100):
    pag.typewrite("I love you " + str(i))
    time.sleep(0.5)
    pag.press("enter")



