def day7_CalculateWeight(tabProgs, indexFather):
    indexSon = []

    for son in xrange(2, len(tabProgs[indexFather])):
        for index in xrange(0, len(tabProgs)):
            if tabProgs[index][0] == tabProgs[indexFather][son]:
                indexSon.append(index)

    for index in indexSon:
        tabProgs[indexFather][1] = tabProgs[indexFather][1] + day7_CalculateWeight(tabProgs, index)

    return tabProgs[indexFather][1]

def day7_CheckWeight(tabProgs, indexFather):
    indexSon = []

    for son in xrange(2, len(tabProgs[indexFather])):
        for index in xrange(0, len(tabProgs)):
            if tabProgs[index][0] == tabProgs[indexFather][son]:
                indexSon.append(index)
    for index in xrange(1, len(indexSon)):
        if tabProgs[indexSon[index]][1] != tabProgs[indexSon[0]][1]:
            for index_ in indexSon:
                print tabProgs[index_][0:2],
            print
            for index_ in indexSon:
                print day7Input.splitlines()[index_].split(' ')[0:2],
            print
            break

    for index in indexSon:
        day7_CheckWeight(tabProgs, index)

def p2():
    tabProgs = []
    nameTop = p1()
    for prog in day7Input.splitlines():
        tabProg = []
        for data in prog.split(' '):
            tabProg.append(data)
        if len(tabProg) > 2:
            del tabProg[2]

        tabProg[1] = int(tabProg[1][1:-1])

        for index in xrange(2, len(tabProg)-1):
            tabProg[index] = tabProg[index][:-1]

        if tabProg[0] == nameTop:
            indexTop = day7Input.splitlines().index(prog)

        tabProgs.append(list(tabProg))

    day7_CalculateWeight(tabProgs, indexTop)
    day7_CheckWeight(tabProgs, indexTop)

def p1():
    tabProgs = []
    for prog in day7Input.splitlines():
        tabProg = []
        for data in prog.split(' '):
            tabProg.append(data)
        if len(tabProg) > 2:
            del tabProg[2]

        tabProg[1] = int(tabProg[1][1:-1])

        for index in xrange(2, len(tabProg)-1):
            tabProg[index] = tabProg[index][:-1]

        tabProgs.append(list(tabProg))

    prog = 0
    while prog < len(tabProgs):
        if len(tabProgs[prog]) == 2:
            del tabProgs[prog]
        else:
            prog = prog + 1

    name = tabProgs[0][0]
    while True:
        newName = ""
        for prog in tabProgs:
            if name in prog:
                if name != prog[0]:
                    newName = prog[0]
                    break
        if newName == "":
            return name
        else:
            name = newName

day7Input = open("day7/input.txt", "r").read()