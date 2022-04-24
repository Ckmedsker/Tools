# Used to combine two word lists together and recieved every possible combination of the two
# This script does not delete the existing text in the output file, but appends it
# Specify below the first and second input files, and an output file
FILE1 = ""
FILE2 = ""
OUT = ""
if FILE1 == "" or FILE2 == "" or OUT == "":
    print("Please specify the correct files.")
    exit()

with open(OUT, "a") as out:
    with open(FILE1, "r") as first:
        flines = first.readlines()
        with open(FILE2, "r") as second:
            slines = second.readlines()
            for fline in flines:
                fline = fline.strip("\n")
                for sline in slines:
                    out.write(f"{fline}{sline}")
