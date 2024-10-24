import pyautogui
import pygetwindow
from PIL import Image

path = r"C:\Users\Dell\PycharmProjects\filehandling\result.png"
titles = pygetwindow.getAllTitles()

window = pygetwindow.getWindowsWithTitle("Command Prompt")[0]
left,top = window.topleft
right,bottom = window.bottomright

pyautogui.screenshot(path)
im = Image.open(path)
im = im.crop((left-10, top-10, right-10, bottom-10))
im.save(path)
im.show(path)

