def p2():
    tot = 0
    lenCap = len(dayInput)
    haslfLenCap = lenCap/2
    for i in xrange(0, len(dayInput) - 1):
        if dayInput[i] == dayInput[(i+haslfLenCap)%lenCap]:
            tot = tot + int(dayInput[i])

    return tot

def p1():
    tot = 0
    for i in xrange(0, len(dayInput) - 1):
        if dayInput[i] == dayInput[i+1]:
            tot = tot + int(dayInput[i])

    if dayInput[0] == dayInput[len(dayInput) - 1]:
        tot = tot + int(dayInput[0])

    return tot

dayTxt = open("day1/input.txt", "r").strip()
dayInput = dayTxt.read()