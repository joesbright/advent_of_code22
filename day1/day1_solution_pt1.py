import numpy as np


myfile = open('data.txt', 'r')
lines = myfile.readlines()

elf_highest = -np.inf
elf_total = 0.

for line in lines:
    if line.strip('\n') == '':
        if elf_total > elf_highest:
            elf_highest = elf_total

        elf_total = 0.
    else:
        elf_total += float(line)

print(elf_highest)