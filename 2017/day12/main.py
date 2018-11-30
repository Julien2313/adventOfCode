import re

def p1():
    data = []
    for prog in day12Input.splitlines():
        data.append(re.split(', | <-> ', prog.strip()))

    groupsConnected = [0]
    getConnections(0, data, groupsConnected)

    return len(groupsConnected)

def getConnections(numProg, data, groupsConnected):
    progs = []
    for prog in data[numProg][1:]:
        progs.append(int(prog))

    for prog in progs:
        if not prog in groupsConnected:
            groupsConnected += [prog]
            getConnections(prog, data, groupsConnected)

def p2():
    data = []
    for prog in day12Input.splitlines():
        data.append(re.split(', | <-> ', prog.strip()))

    connections = [-1]*len(data)

    for numProg in xrange(0, len(data)):
        if not connections[numProg] == -1:
            continue

        groupsConnected = [numProg]
        getConnections(numProg, data, groupsConnected)

        for group in groupsConnected:
            connections[group] = numProg

    return len(set(connections))

day12Input = open("day12/input.txt", "r").read().strip()
