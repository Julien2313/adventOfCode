
def p2():
    lengths = []
    for x in xrange(0, len(day10Input) - 1):
        lengths.append(ord(day10Input[x]))

    lengths += [17, 31, 73, 47, 23]
    tabNumber = list(range(256))

    currentPos = 0
    skipSize = 0
    for x in xrange(0, 64):
        for lenght in lengths:
            for step in xrange(0, lenght // 2):
                index1 = (currentPos + step) % len(tabNumber)
                index2 = (currentPos + lenght - 1 - step) % len(tabNumber)
                tabNumber[index1], tabNumber[index2] = tabNumber[index2], tabNumber[index1]

            currentPos += lenght + skipSize
            skipSize += 1

    hash = ""
    for i in range(len(tabNumber) // 16):
        numDec = tabNumber[i * 16 + 15]
        for j in range(15):
            numDec ^= tabNumber[i * 16 + j]
        hash += hex(numDec)[2:].zfill(2)

    return hash

def p1():

    tabNumber = list(range(256))

    currentPos = 0
    skipSize = 0

    for lenghtString in day10Input.split(','):
        lenght = int(lenghtString)
        for step in xrange(0, lenght // 2):
            index1 = (currentPos + step) % len(tabNumber)
            index2 = (currentPos + lenght - 1 - step) % len(tabNumber)
            tabNumber[index1], tabNumber[index2] = tabNumber[index2], tabNumber[index1]

        currentPos += lenght + skipSize
        skipSize += 1

    return tabNumber[0] * tabNumber[1]

day10Input = open("day10/input.txt", "r").read()