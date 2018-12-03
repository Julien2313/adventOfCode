from collections import Counter

def p2():
    playground = [[0 for x in range(1000)] for y in range(1000)]
    allIDs = [x+1 for x in range(1293)]
    for line in dayInput.splitlines():
        ID = int(line.split(' ')[0][1:])
        x1 = int(line.split(' ')[2].split(',')[0])
        y1 = int(line.split(' ')[2].split(',')[1][:-1])
        x2 = int(line.split(' ')[3].split('x')[0])
        y2 = int(line.split(' ')[3].split('x')[1])
        for x in xrange(x2):
            for y in xrange(y2):
                if (playground[x1+x][y1+y] != 0):
                    try:
                        allIDs.remove(playground[x1+x][y1+y])
                    except:
                        pass
                    try:
                        allIDs.remove(ID)
                    except:
                        pass
                playground[x1+x][y1+y]=ID
    return allIDs

def p1():
    playground = [[0 for x in range(1000)] for y in range(1000)] 
    for line in dayInput.splitlines():
        x1 = int(line.split(' ')[2].split(',')[0])
        y1 = int(line.split(' ')[2].split(',')[1][:-1])
        x2 = int(line.split(' ')[3].split('x')[0])
        y2 = int(line.split(' ')[3].split('x')[1])
        for x in xrange(x2):
            for y in xrange(y2):
                playground[x1+x][y1+y]+=1
    cpt = 0
    for x in xrange(1000):
        for y in xrange(1000):
            if playground[x][y] > 1:
                cpt +=1
    return cpt
        
dayFile = open("day3/input.txt", "r")
dayInput = dayFile.read().strip()
