# This program is made primarily to make it easier to take screenshots quickly
import pyautogui
from pynput import keyboard
from time import sleep
from pygame import mixer
import os

# Start X, Start Y, End X, End Y
location = r"C:\Users\Camer\Desktop\SDEVDegree\Intro to Software Development\Module8"
SS = [0, 0, 1600, 860]
again = ""
sound = "Gb2.mp3"
mixer.init()


os.system('cls' if os.name == 'nt' else 'clear')
name = input("Enter the image name:\n")
print("Hit h to screenshot!")


def quit_program():
    exit()


def on_start():
    screenshot = pyautogui.screenshot(region=(SS[0], SS[1], SS[2], SS[3]))
    screenshot.save(f"{location}\{name}.png")
    mixer.music.load(sound)
    mixer.music.play()
    sleep(1)
    exit()


with keyboard.GlobalHotKeys({
        '<ctrl>+c': quit_program,
        'h': on_start}) as h:
    h.join()
