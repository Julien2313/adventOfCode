def checkRule(rule, gen):
    match=[]
    for cpt in xrange(len(gen)):
        if gen[cpt:cpt+5] == rule:
            match.append(cpt)
    return match

def computeScore(marge, gen):
    return sum([x-marge for x in xrange(len(gen)) if gen[x]])

def computeDelta(marge1, gen1, marge2, gen2):
    return computeScore(marge1, gen1)-computeScore(marge2, gen2)


def p2():
    initState = [c for c in dayInput.splitlines()[0].split("initial state: ")[1]]
    margesLeft = [0]

    rules = []
    states = [[c=="#" for c in initState]]

    for line in dayInput.splitlines()[2:]:
        rule, result = line.split(" => ")
        if result == "#":
            rules.append([c=="#" for c in rule])

    gen = 1
    while True:
        margesLeft.append(margesLeft[-1])
        while states[-1][:4] != [False]*4:
            states[-1] = [False]+states[-1]
            margesLeft[-1]+=1

        while states[-1][-4:] != [False]*4:
            states[-1] = states[-1]+[False]

        states.append([False] * len(states[-1]))
        for rule in rules:
            matchs = checkRule(rule, states[-2])
            for match in matchs:
                states[-1][match+2] = True
        if gen > 3:
            if computeDelta(margesLeft[-1], states[-1], margesLeft[-2], states[-2]) == computeDelta(margesLeft[-2], states[-2], margesLeft[-3], states[-3]):
                break
        gen+=1
    delta = computeDelta(margesLeft[-1], states[-1], margesLeft[-2], states[-2])
    lastScore = computeScore(margesLeft[-1], states[-1])
    return (50000000000-gen) * delta + lastScore

def p1():
    initState = [c for c in dayInput.splitlines()[0].split("initial state: ")[1]]
    margeLeft = 0

    rules = []
    states = [[c == "#" for c in initState]]

    for line in dayInput.splitlines()[2:]:
        rule, result = line.split(" => ")
        if result == "#":
            rules.append([c == "#" for c in rule])

    for gen in xrange(1, 21):
        while states[-1][:4] != [False]*4:
            states[-1] = [False]+states[-1]
            margeLeft+=1

        while states[-1][-4:] != [False]*4:
            states[-1] = states[-1] + [False]

        states.append([False]*len(states[-1]))
        for rule in rules:
            matchs = checkRule(rule, states[-2])
            for match in matchs:
                states[gen][match+2] = True
    return computeScore(margeLeft, states[-1])

dayFile = open("day12/input.txt", "r")
dayInput = dayFile.read().strip()
