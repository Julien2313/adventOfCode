
def p1():
    progs = list("abcdefghijklmnop")

    for move in day16Input.split(','):
        if move[0] == 'x':
            index1, index2 = map(int, move[1:].split('/'))
            progs[index1], progs[index2] = progs[index2], progs[index1]

        elif move[0] == 's':
            x = int(move[1:])
            progs = progs[-x:] + progs[:-x]

        elif move[0] == 'p':
            strIndex1, strIndex2 = move[1:].split('/')
            index1 = progs.index(strIndex1)
            index2 = progs.index(strIndex2)
            progs[index1], progs[index2] = progs[index2], progs[index1]


    return ''.join(progs)

def p2():
    progs = list("abcdefghijklmnop")
    dancesSow = []
    for dance in xrange(0, 1000000000):
        currentDance = ''.join(progs)
        if currentDance in dancesSow:
            return dancesSow[1000000000 % dance]
        dancesSow.append(currentDance)

        for move in day16Input.split(','):
            if move[0] == 'x':
                index1, index2 = map(int, move[1:].split('/'))
                progs[index1], progs[index2] = progs[index2], progs[index1]

            elif move[0] == 's':
                x = int(move[1:])
                progs = progs[-x:] + progs[:-x]

            elif move[0] == 'p':
                strIndex1, strIndex2 = move[1:].split('/')
                index1 = progs.index(strIndex1)
                index2 = progs.index(strIndex2)
                progs[index1], progs[index2] = progs[index2], progs[index1]

    return ''.join(progs)


day16Input = open("day16/input.txt", "r").read().strip()
