# This program is used to generator all possible combinations of numbers up to a certain amount
OUT = ""
if OUT == "":
    print("Please specify an output file!")
    exit()
num = [0,1,2,3,4,5,6,7,8,9]

# below there is three for loops to generate numbers 000-999,
# you can add/remove for loops for different lengths of digits

with open(OUT, "w") as output:
    for one in num:
        for two in num:
            for three in num:
                # when adding/removing for loops, edit the line below
                output.write(f"{one}{two}{three}\n") 
