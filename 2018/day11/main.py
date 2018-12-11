def p2():
    playground = [[0 for x in xrange(301)] for y in xrange(301)]
    serial = int(dayInput)

    for x in xrange(1, 301):
        for y in xrange(1, 301):
            rackID = x + 10
            powerLevel = rackID * y
            powerLevel += serial
            powerLevel *= rackID
            hundred = (powerLevel//100)%10
            level = hundred - 5
            playground[x][y] = level

    maxi = 0
    X, Y, SIZE = 0, 0, 0
    for x in xrange(1, 301):
        for y in xrange(1, 301):
            maxSize = 300 - max(x, y)
            totSubSize = 0
            for size in xrange(0, maxSize):
                for dx in xrange(x, x+size):
                    totSubSize += playground[dx][y+size]
                totSubSize += sum(playground[x+size][y:y+size])
                totSubSize += playground[x+size][y+size]
                if totSubSize > maxi:
                    maxi = totSubSize
                    X = x
                    Y = y
                    SIZE = size+1
    return (X, Y, SIZE)

def p1():
    playground = [[0 for x in xrange(301)] for y in xrange(301)]
    serial = int(dayInput)

    for x in xrange(1, 301):
        for y in xrange(1, 301):
            rackID = x + 10
            powerLevel = rackID * y
            powerLevel += serial
            powerLevel *= rackID
            hundred = (powerLevel//100)%10
            level = hundred - 5
            playground[x][y] = level
    max = 0
    X, Y = 0, 0
    for x in xrange(1, 298):
        for y in xrange(1, 298):
            tot = 0
            for dx in xrange(x, x+3):
                tot += sum(playground[dx][y:y+3])
            if tot > max:
                max = tot
                X = x
                Y = y
    return (X, Y)


dayFile = open("day11/input.txt", "r")
dayInput = dayFile.read().strip()
