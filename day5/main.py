def p2():
    tab = day5Input.splitlines()
    index = 0
    cpt = 0

    while True:
        cpt = cpt + 1
        nextIndex = int(tab[index]) + index

        if int(tab[index]) >= 3:
            tab[index] = int(tab[index]) - 1
        else:
            tab[index] = int(tab[index]) + 1

        index = nextIndex
        if index >= len(tab):
            break
    return cpt

def p1():
    tab = day5Input.splitlines()
    index = 0
    cpt = 0

    while True:
        cpt = cpt + 1
        nextIndex = int(tab[index]) + index

        tab[index] = int(tab[index]) + 1

        index = nextIndex
        if index >= len(tab):
            break
    return cpt


day5Input = open("day5/input.txt", "r").read()