# This program was made to random print out as many items in a file as the user would like
import os
import random

REL_PATH = os.path.dirname(__file__)
os.system('cls' if os.name == 'nt' else 'clear')
file = input("Please enter the name of the .txt file you wish to take random items from:\n")
numb_of_items = int(input("How many items would you like to randomly select?: "))


with open(f"{REL_PATH}\{file}", "r") as info:
    lines = info.readlines()
    numb_of_lines = len(lines)
    for index, line in enumerate(lines):
        lines[index] = line.strip("\n")
    for index in range(0, numb_of_items):
        random_item = random.randrange(0,numb_of_lines)
        print(lines[random_item])
