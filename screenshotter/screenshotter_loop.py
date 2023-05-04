# This program is made primarily to make it easier to take screenshots quickly
import pyautogui
from pynput import keyboard
from time import sleep
from pygame import mixer
import os

# Start X, Start Y, End X, End Y
location = r"C:\Users\Camer\Desktop\SDEVDegree\Test"
SS = [200, 100, 1720, 780]
again = ""
sound = "Gb2.mp3"
mixer.init()


def quit_program():
    exit()


def on_start(name):
    screenshot = pyautogui.screenshot(region=(SS[0], SS[1], SS[2], SS[3]))
    screenshot.save(f"{location}\{name}.png")
    mixer.music.load(sound)
    mixer.music.play()
    sleep(2)


for numb in range(1, 21):
    on_start(numb)
    print(numb)


# with keyboard.GlobalHotKeys({
#         '<ctrl>+c': quit_program,
#         'h': on_start}) as h:
#     h.join()
