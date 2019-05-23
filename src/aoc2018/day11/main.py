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
            playground[x][y] = hundred - 5

    sums = [[0 for x in xrange(301)] for y in xrange(301)]
    for x in xrange(1, 300):
        for y in xrange(1, 300):
            sums[x][y] = sums[x-1][y] + sums[x][y-1] - sums[x-1][y-1] + playground[x][y]

    maxi = 0
    X, Y, SIZE = 0, 0, 0
    for x in xrange(1, 301):
        for y in xrange(1, 301):
            maxSize = 300 - max(x, y)
            for size in xrange(0, maxSize):
                area = sums[x-1][y-1] + sums[x+size][y+size] - sums[x-1][y+size] - sums[x+size][y-1] 
                if area > maxi:
                    maxi = area
                    X = x
                    Y = y
                    SIZE = size+1

    return str(X)+","+ str(Y)+","+ str(SIZE)

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
            playground[x][y] = hundred - 5
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
    return str(X)+","+ str(Y)


dayFile = open("day11/input.txt", "r")
dayInput = dayFile.read().strip()
