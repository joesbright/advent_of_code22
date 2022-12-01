import numpy as np

def sort_array_bubble(myarray):

    newarray = myarray
    sorted = True

    for i in range(len(newarray)):
        if i + 1 == len(newarray):
            break
        elif newarray[i+1] >= newarray[i]:
            continue
        elif newarray[i+1] < newarray[i]:
            newarray[i+1], newarray[i] = newarray[i], newarray[i+1]
            sorted = False

    if sorted == True:
        return newarray
    elif sorted == False:
        return sort_array_bubble(newarray)




myfile = open('data.txt', 'r')
lines = myfile.readlines()

elf_total = 0.

totals = []

for line in lines:
    if line.strip('\n') == '':
        totals.append(elf_total)
        elf_total = 0.
    else:
        elf_total += float(line)

print(sort_array_bubble(totals))
print(sort_array_bubble(totals)[-1] + sort_array_bubble(totals)[-2] + sort_array_bubble(totals)[-3])