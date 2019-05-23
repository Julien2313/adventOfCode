import re

def p2():
    return

def p1():
    playground = []
    for line in dayInput.splitlines():
        pos1, pos2 = line.split("> velocity=<")
        pos1 = map(int, pos1[10:].split(","))
        pos2 = map(int, pos2[:-1].split(","))
        playground.append([pos1, pos2])
        # x1, y1, x2, y2 = map(int, re.findall(r'-?\d+', line))
        # playground.append([[x1, y1], [x2, y2]])

    minTemps = 0
    minArea = 9999999

    for deltaT in xrange(40000):
        minx = min(x1 + deltaT * x2 for ((x1, _ )), ((x2, _ )) in playground)
        maxx = max(x1 + deltaT * x2 for ((x1, _ )), ((x2, _ )) in playground)
        miny = min(y1 + deltaT * y2 for ((_ , y1)), ((_ , y2)) in playground)
        maxy = max(y1 + deltaT * y2 for ((_ , y1)), ((_ , y2)) in playground)
        area = (maxx-minx) * (maxy-miny)
        if area < minArea:
            minArea = area
            minTemps = deltaT

    playground2 = [[' '] * 300 for y in xrange(300)]
    for ((x1, y1), (x2, y2)) in playground:
        playground2[y1 + minTemps * y2][x1 + minTemps * x2] = 'X'

    for line in playground2:
        if (''.join(line)).count(" ") == len(line):
            continue
        print ''.join(line)
    return minTemps

dayFile = open("day10/input.txt", "r")
dayInput = dayFile.read().strip()
