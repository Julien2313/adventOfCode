import numpy as np
import day10.main as prob2

def p1():
    cpt = 0
    for x in xrange(0, 128):
        chaine = prob2.p2(day14Input + '-' + str(x))
        cpt += bin(int(chaine, 16))[2:].zfill(4*len(chaine)).count('1')
    return cpt

def p2CheckGroup(x, y, grille, group):
    if grille[x][y] == 0:
        grille[x][y] = group
        if x > 0:
            p2CheckGroup(x - 1, y, grille, group)
        if y > 0:
            p2CheckGroup(x, y - 1, grille, group)
        if x < 127:
            p2CheckGroup(x + 1, y, grille, group)
        if y < 127:
            p2CheckGroup(x, y + 1, grille, group)

def p2():
    grille = np.ndarray((128,128))
    for x in xrange(0, 128):
        chaine = prob2.p2(day14Input + '-' + str(x))
        binar = bin(int(chaine, 16))[2:].zfill(4*len(chaine))
        for digit in xrange(0, 128):
            if binar[digit] == '0':
                grille[x][digit] = -1
            else:
                grille[x][digit] = 0
    group = 0
    for x in xrange(0, 128):
        for y in xrange(0, 128):
            if grille[x][y] == 0:
                group += 1
                p2CheckGroup(x, y, grille, group)
    return group

day14Input = open("day14/input.txt", "r").read().strip()
