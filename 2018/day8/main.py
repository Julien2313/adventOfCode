
def recur2(data):
    child, metadada = data[:2]
    data = data[2:]
    scores = []
    tot = 0

    for i in xrange(child):
        totChild, score, data = recur2(data)
        tot += totChild
        scores.append(score)

    tot += sum(data[:metadada])

    if child == 0:
        return tot, tot, data[metadada:]
    else:
        scoresChild = []
        for child in data[:metadada]:
            if child > 0 and child <= len(scores):
                scoresChild.append(scores[child - 1])

        score = sum(scoresChild)
        
        return tot, score, data[metadada:]

def recur(data):
    child = data[0]
    nbrMetadada = data[1]

    data = data[2:]
    tot = 0

    for i in xrange(child):
        totChild, data = recur(data)
        tot += totChild

    tot += sum(data[:nbrMetadada])

    return tot, data[nbrMetadada:]

def p2():
    data = map(int,dayInput.split(' '))   

    return recur2(data)[1]

def p1():
    data = map(int,dayInput.split(' '))   

    return recur(data)[0]

tot = 0

dayFile = open("day8/input.txt", "r")
dayInput = dayFile.read().strip()
