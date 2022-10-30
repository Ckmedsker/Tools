# This program is used to get a user selected amount of random files from a given directory. Not finished.
import os
import random

REL_PATH = os.path.dirname(__file__)
selected_file_list = []


os.system('cls' if os.name == 'nt' else 'clear')
folder = input("Please select a folder based from this directory!\nIf you choose to select from this folder, press enter!: ")
if folder != "":
    folder = (fr"\{folder}")
files = os.listdir(fr"{REL_PATH}{folder}")
files_count = len(files)
print(f"There is {files_count} files in this directory!")

while True:
    numb_of_files = int(input("How many files would you like to randomly select?: "))
    if numb_of_files <= 0:
        print("Cannot select less than or equal to 0 files. Try again.")
    elif numb_of_files >= files_count:
        print(f"There is {files_count} files in this directory!")
        print("Cannot select more files than exist in the directory! Try again.")
    else:
        break


for index in range(0, numb_of_files):
    print(files[random.randint(0, len(files))])