# This program was made to random print out as many items in a file as the user would like
import os
import random

REL_PATH = os.path.dirname(__file__)
os.system('cls' if os.name == 'nt' else 'clear')
file = input("Please enter the name of the .txt file you wish to take random items from:\n")


with open(f"{REL_PATH}\{file}", "r") as info:
    lines = info.readlines()
    numb_of_lines = len(lines)
    numb_of_items = int(input(f"How many items would you like to randomly select? Max {numb_of_lines}: "))
    for index, line in enumerate(lines):
        lines[index] = line.strip("\n")
    for item in random.sample(lines, numb_of_items):
        print(item)
