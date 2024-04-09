import pyautogui as pag
import time
# image = 'images/cactus.png'
# image = "images/setting.png"
# image = "images/extention.png"
image = 'images/excel2.png'
# image = 'images/docker.png'
pag.useImageNotFoundException()
try:
    findImage = pag.locateOnScreen(image, confidence =0.6)
    print((findImage))
    pag.click(findImage)
except pag.ImageNotFoundException:
    print('ImageNotFoundException: image not found')