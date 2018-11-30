
def p1():
    values = [0]
    nbrSteps = 382
    pos = 0

    for step in xrange(1, 2018):
        pos = (pos + nbrSteps) % len(values) + 1
        values.insert(pos, step)
    return values[values.index(2017) + 1]

def p2():
    nbrSteps = 382
    pos = 0
    for step in xrange(1,50000001):
        pos = (pos + nbrSteps) % step + 1
        if pos == 1:
            valuePos1 = step
    return valuePos1


day17Input = open("day17/input.txt", "r").read().strip()
