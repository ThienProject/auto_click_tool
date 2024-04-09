import pyautogui as pag
import time
# time.sleep(5)
# x, y , width , height
screen = pag.screenshot(region=(0, 0, 300, 800))
screen.save("images/p3.png")
print("ok")