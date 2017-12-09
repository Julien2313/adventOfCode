def p2():
    tot = 0
    lenCap = len(day1Input)
    haslfLenCap = lenCap/2
    for i in xrange(0, len(day1Input) - 1):
        if day1Input[i] == day1Input[(i+haslfLenCap)%lenCap]:
            tot = tot + int(day1Input[i])

    return tot

def p1():
    tot = 0
    for i in xrange(0, len(day1Input) - 1):
        if day1Input[i] == day1Input[i+1]:
            tot = tot + int(day1Input[i])

    if day1Input[0] == day1Input[len(day1Input) - 1]:
        tot = tot + int(day1Input[0])

    return tot

day1Txt = open("day1/input.txt", "r")
day1Input = day1Txt.read()