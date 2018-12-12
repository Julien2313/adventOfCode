def checkRule(rule, gen):
    match=[]
    for cpt in xrange(len(gen)):
        if gen[cpt:cpt+5] == rule:
            match.append(cpt)
    return match

def computeScore(marge, gen):
    return sum([x-marge for x in xrange(len(gen)) if gen[x] == "#"])

def computeDelta(marge1, gen1, marge2, gen2):
    return computeScore(marge1, gen1)-computeScore(marge2, gen2)


def p2():
    initState = [c for c in dayInput.splitlines()[0].split("initial state: ")[1]]
    margesLeft = [0]

    rules = []
    states = [initState]

    for line in dayInput.splitlines()[2:]:
        rule, what = line.split(" => ")
        if what == "#":
            rules.append([c for c in rule])

    x = 1
    while True:
        margesLeft.append(margesLeft[-1])
        while ''.join(states[x-1][:4]) != "....":
            states[x-1] = ["."]+states[x-1]
            margesLeft[-1]+=1

        while ''.join(states[x-1][-4:]) != "....":
            states[x-1] = states[x-1]+["."]

        states.append(["."]*len(states[x-1]))
        for rule in rules:
            matchs = checkRule(rule, states[x-1])
            for match in matchs:
                states[x][match+2] = "#"
        if x > 10:
            if computeDelta(margesLeft[-1], states[-1], margesLeft[-2], states[-2]) == computeDelta(margesLeft[-2], states[-2], margesLeft[-3], states[-3]):
                break
        x+=1
    return (50000000000-x)*computeDelta(margesLeft[-1], states[-1], margesLeft[-2], states[-2])+sum([x-margesLeft[-1] for x in xrange(len(states[-1])) if states[-1][x] == "#"])
        


def p1():
    initState = [c for c in dayInput.splitlines()[0].split("initial state: ")[1]]
    margeLeft = 0

    rules = []
    states = [initState]

    for line in dayInput.splitlines()[2:]:
        rule, what = line.split(" => ")
        if what == "#":
            rules.append([c for c in rule])


    for x in xrange(1, 21):
        while ''.join(states[x-1][:4]) != "....":
            states[x-1] = ["."]+states[x-1]
            margeLeft+=1

        while ''.join(states[x-1][-4:]) != "....":
            states[x-1] = states[x-1]+["."]

        states.append(["."]*len(states[x-1]))
        for rule in rules:
            matchs = checkRule(rule, states[x-1])
            for match in matchs:
                states[x][match+2] = "#"
    return sum([x-margeLeft for x in xrange(len(states[-1])) if states[-1][x] == "#"])


dayFile = open("day12/input.txt", "r")
dayInput = dayFile.read().strip()
