# This script is used to append various items to the end of every line in a file
# Most likely used for creating custom wordlists
# Specific below the input file and output file (they can be the same but it is not recommended)
FILE1 = ""
OUT = "" 
if FILE1 == "" or OUT == "":
    print("Please specify the correct files.")
    exit()


# If other characters are to be appended, you can edit these values.
num = [0,1,2,3,4,5,6,7,8,9]
sym = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|',
',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#','$', ')', '/']


def main(var):
    with open(FILE1, "r") as items:
        with open(OUT, "a") as add:
            lines = items.readlines()
            for i in var: 
                for line in lines:
                    line = line.strip("\n")
                    add.write(f"{line}{i}\n")


mode = int(input("What do you want to append to end of lines?\n1 for numbers\n2 for symbols\n3 for both\n\n"))
if mode == 1:
    main(num)
elif mode == 2:
    main(sym)
elif mode == 3:
    with open(FILE1, "r") as items:
        with open(OUT, "a") as add:
            lines = items.readlines()
            for i in num:
                for j in sym:
                    for line in lines:
                        line = line.strip("\n")
                        add.write(f"{line}{i}{j}\n")
            for k in num:
                for h in sym:
                    for line in lines:
                        line = line.strip("\n")
                        add.write(f"{line}{h}{k}\n")
else:
    exit()
