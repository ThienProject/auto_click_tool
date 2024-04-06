import pyautogui as pag
import time
# image = 'cactus.png'
# image = "setting.png"
# image = "extention.png"
image = 'excel2.png'
# image = 'docker.png'
pag.useImageNotFoundException()
try:
    findImage = pag.locateOnScreen(image, confidence =0.6)
    print((findImage))
    pag.click(findImage)
except pag.ImageNotFoundException:
    print('ImageNotFoundException: image not found')