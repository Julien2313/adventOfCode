import numpy as np
import day10.main as prob2

def p1():
    cpt = 0
    for x in xrange(0, 128):
        chaine = prob2.p2(day14Input + '-' + str(x))
        cpt += bin(int(chaine, 16))[2:].zfill(4*len(chaine)).count('1')
    return cpt

def p2CheckGroup(x, y, grille):
    if grille[x][y]:
        grille[x][y] = False
        if x > 0:
            p2CheckGroup(x - 1, y, grille)
        if y > 0:
            p2CheckGroup(x, y - 1, grille)
        if x < 127:
            p2CheckGroup(x + 1, y, grille)
        if y < 127:
            p2CheckGroup(x, y + 1, grille)

def p2():
    grille = np.ndarray((128,128))
    for x in xrange(0, 128):
        chaine = prob2.p2(day14Input + '-' + str(x))
        binar = bin(int(chaine, 16))[2:].zfill(4*len(chaine))
        for digit in xrange(0, 128):
            if binar[digit] == '0':
                grille[x][digit] = False
            else:
                grille[x][digit] = True

    group = 0
    for x in xrange(0, 128):
        for y in xrange(0, 128):
            if grille[x][y]:
                group += 1
                p2CheckGroup(x, y, grille)
    return group

day14Input = open("day14/input.txt", "r").read().strip()
