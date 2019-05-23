def recurp2(data):
    nbrChild = data[0]
    nbrRef = data[1]

    tot = 0
    data = data[2:]
    
    children = []

    for child in xrange(nbrChild):
        data, score = recurp2(data)
        children.append(score)

    if nbrChild == 0:
        tot += sum(data[:nbrRef])
        return data[nbrRef:], tot

    tot=0
    for child in data[:nbrRef]:
        if child > 0 and child <= len(children):
            tot += children[child-1]

    return data[nbrRef:], tot

def recurp1(data):
    nbrChild = data[0]
    nbrMetadata = data[1]

    tot = 0
    data = data[2:]

    for child in xrange(nbrChild):
        data, totChild = recurp1(data)
        tot += totChild

    tot += sum(data[:nbrMetadata])
    return data[nbrMetadata:], tot


def p2():
    data = map(int,dayInput.split(' '))   

    return recurp2(data)[1]

def p1():
    data = map(int,dayInput.split(' '))   

    return recurp1(data)[1]

tot = 0

dayFile = open("day8/input.txt", "r")
dayInput = dayFile.read().strip()