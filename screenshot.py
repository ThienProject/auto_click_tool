import pyautogui as pag
import time
time.sleep(5)
screen = pag.screenshot()
screen.save("images/p2.png")
print("ok")