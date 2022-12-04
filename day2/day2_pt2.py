import pandas as pd


def calc_score(p1, p2):
    # A : ROCK : 1
    # B : PAPER : 2
    # C : SCISSORS : 3

    # X : ROCK
    # Y : PAPER
    # Z : SCISSORS

    p1_score = 0
    p2_score = 0

    # MAKE UNIFORM
    if p1 == 'A':
        p1 = 'X'
    elif p1 == 'B':
        p1 = 'Y'
    elif p1 == 'C':
        p1 = 'Z'

    if (p1 == 'X') and (p2 == 'Y'):
        p1_score += 1
        p2_score += 2 + 6
    if (p1 == 'X') and (p2 == 'Z'):
        p1_score += 1 + 6
        p2_score += 3
    if (p1 == 'Y') and (p2 == 'X'):
        p1_score += 2 + 6
        p2_score += 1
    if (p1 == 'Y') and (p2 == 'Z'):
        p1_score += 2
        p2_score += 3 + 6
    if (p1 == 'Z') and (p2 == 'X'):
        p1_score += 3
        p2_score += 1 + 6
    if (p1 == 'Z') and (p2 == 'Y'):
        p1_score += 3 + 6
        p2_score += 2
    if (p1 == 'X') and (p2 == 'X'):
        p1_score += 1 + 3
        p2_score += 1 + 3
    if (p1 == 'Y') and (p2 == 'Y'):
        p1_score += 2 + 3
        p2_score += 2 + 3
    if (p1 == 'Z') and (p2 == 'Z'):
        p1_score += 3 + 3
        p2_score += 3 + 3

    return p1_score, p2_score

def calc_play(p1, p2):
    # A : ROCK
    # B : PAPER
    # C : SCISSORS

    # X : LOSE
    # Y : DRAW
    # Z : WIN

    p1_score = 0
    p2_score = 0

    # MAKE UNIFORM
    if p1 == 'A':
        p1 = 'X'
    elif p1 == 'B':
        p1 = 'Y'
    elif p1 == 'C':
        p1 = 'Z'

    if (p1 == 'X') and (p2 == 'Y'):
        p1_score += 1 + 3
        p2_score += 1 + 3
    if (p1 == 'X') and (p2 == 'Z'):
        p1_score += 1
        p2_score += 2 + 6
    if (p1 == 'Y') and (p2 == 'X'):
        p1_score += 2 + 6
        p2_score += 1
    if (p1 == 'Y') and (p2 == 'Z'):
        p1_score += 2
        p2_score += 3 + 6
    if (p1 == 'Z') and (p2 == 'X'):
        p1_score += 3 + 6
        p2_score += 2
    if (p1 == 'Z') and (p2 == 'Y'):
        p1_score += 3 + 3
        p2_score += 3 + 3
    if (p1 == 'X') and (p2 == 'X'):
        p1_score += 1 + 6
        p2_score += 3
    if (p1 == 'Y') and (p2 == 'Y'):
        p1_score += 2 + 3
        p2_score += 2 + 3
    if (p1 == 'Z') and (p2 == 'Z'):
        p1_score += 3
        p2_score += 1 + 6

    return p1_score, p2_score

data = pd.read_csv('data.txt', header=None, delim_whitespace=True, names=['p1', 'p2'])

myscore = 0
for index, row in data.iterrows():
    myscore += calc_score(row['p1'], row['p2'])[1]
print(myscore)

myscore = 0
for index, row in data.iterrows():
    myscore += calc_play(row['p1'], row['p2'])[1]
print(myscore)