# This script is used to substitute all specified characters for all other
# specified characters in a given file
# Below specify the file to read from, a temp file and an output file
FILE1 = ""
TEMP = ""
OUTPUT = ""
if FILE1 == "" or TEMP == "" or OUTPUT == "":
    print("Please specify the correct files.")
    exit()
lines2 = []
with open(FILE1, "r") as init:
    items = init.readlines()
    with open(TEMP, "w") as init2:
        for i in items:
            init2.write(i)
            print(i.strip("\n"))
        print("\n\n")

def wtemp():
    with open(TEMP, "w") as temp:
        temp.write(''.join(lines2))

def substitute():
    find = str(input("Please enter an item to substitute!\n"))
    replace = str(input("Enter what to replace it with!\n"))
    with open(TEMP, "r") as items:
        lines = items.readlines()
        for line in lines:
            char = list(line)
            for i,j in enumerate(char):
                if j == find:
                    char.pop(i)
                    char.insert(i, replace)
            lines2.append(''.join(char))
    wtemp()
    with open(TEMP, "r") as pr:
        test = pr.readlines()
        for p in test:
            print(p.strip("\n"))
        print("\n\n")

mode = str(input("Do you want to change multiple characters? y/n\n"))
if mode == "n":
    substitute()
    add = str(input("Do you want to write to the list?\n"))
    if add == "y" or add == "":
        with open(TEMP, "r") as pr:
            test = pr.readlines()
            print("Successfully added:\n\n")
            for p in test:
                print(p.strip("\n"))
        with open(OUTPUT, "a") as out:
            for r in test:
                out.write(r)
elif mode == "y" or mode == "":
    while True:
        add = str(input("Do you want to write to the list?\n"))
        if add == "y" or add == "":
            with open(TEMP, "r") as pr:
                test = pr.readlines()
                print("Successfully added:\n\n")
                for p in test:
                    print(p.strip("\n"))
            with open(OUTPUT, "a") as out:
                for r in test:
                    out.write(r)
        again = str(input("Do you want to substitute again? y/n\n"))
        if again == "y" or again == "":
            substitute()
        else:
            with open(TEMP, "r") as pr:
                test = pr.readlines()
                for p in test:
                    print(p.strip("\n"))
                print("\n\n")
            exit()
else:
    exit()
