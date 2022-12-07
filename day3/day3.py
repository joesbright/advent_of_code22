import string
import numpy as np

def assign_score(part1, part2):

    myoverlap = []
    priority = 0

    unique_p1 = set(part1)
    unique_p2 = set(part2)

    for item1 in unique_p1:
        for item2 in unique_p2:
            if item1 == item2:
                myoverlap.append(item1)

    myoverlap = set(myoverlap)

    for item in myoverlap:
        priority += get_score(item)

    return priority

def get_score(letter):
    score = 0
    lower_alphabet = list(string.ascii_lowercase)
    lower_score = np.arange(1, 27, 1)
    upper_alphabet = list(string.ascii_uppercase)
    upper_score = np.arange(27, 53, 1)

    for i, item in enumerate(lower_alphabet):
        if letter == item:
            score += lower_score[i]
    for i, item in enumerate(upper_alphabet):
        if letter == item:
            score += upper_score[i]
    return score

myfile = open('data.txt', 'r')
lines = myfile.readlines()

total_score = 0
for line in lines:
    line = line.strip('\n')
    mylen = len(line)
    p1 = line[0:int(mylen/2)]
    p2 = line[int(mylen/2):]

    total_score += assign_score(p1, p2)

print(total_score)