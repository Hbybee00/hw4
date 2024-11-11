#Hayden Bybee
#Lab Section: 16
#Submission Date: 11/11/24
#Help received from: 
#My brother (again) helped me figure out why my code was 'doubling' for every line and outputting demon horse

from pathlib import Path
path = Path('prompt.txt')
contents = path.read_text()

dictionary1 = {"w":" ","*":"*"}

lines = contents.splitlines()
outp = ""
dictionary2 = {}
pairs = []
outputpath = Path('output.txt')
newfile = ""

for line in lines:
    pairs = line.split("\t")
    for pair in pairs:
        lst = pair.split(":")
        if len(lst) == 2:
            key = lst[0]
            value = lst[1]
            dictionary2[key] = int(value)
        for keys, values in dictionary2.items():
            if keys == "w":
                outp += " "*values
            elif keys == "*":
                outp += "*"*values
        dictionary2 = {}
    newfile += outp + "\n"
    outp = ""

outputpath.write_text(newfile)