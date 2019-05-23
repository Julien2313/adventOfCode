# stats : start 20h03
# 20h22
# 20h24

import re
from collections import defaultdict

def p2():
    playground = [[0 for x in xrange(0, 1000)]for y in xrange(0, 1000)]
    for line in dayInput.splitlines():
        if "toggle" in line:
            
            x1, y1, x2, y2 = map(int, re.findall(r'\d+', line))
            for x in xrange(x1, x2+1):
                for y in xrange(y1, y2+1):
                    playground[x][y] += 2
        else:
            state = -1
            if "on" in line:
                state = 1
                
            x1, y1, x2, y2 = map(int, re.findall(r'\d+', line))
            for x in xrange(x1, x2+1):
                for y in xrange(y1, y2+1):
                    if playground[x][y] > 0 or state == 1:
                        playground[x][y] += state
    count = 0
    for x in xrange(0, 1000):
        for y in xrange(0, 1000):
            count += playground[x][y]
    return count


def p1():
    playground = [[False for x in xrange(0, 1000)]for y in xrange(0, 1000)]
    for line in dayInput.splitlines():
        if "toggle" in line:
            x1, y1, x2, y2 = map(int, re.findall(r'\d+', line))
            for x in xrange(x1, x2+1):
                for y in xrange(y1, y2+1):
                    playground[x][y] = not playground[x][y]
        else:
            state = False
            if "on" in line:
                state = True
                
            x1, y1, x2, y2 = map(int, re.findall(r'\d+', line))
            for x in xrange(x1, x2+1):
                for y in xrange(y1, y2+1):
                    playground[x][y] = state
    count = 0
    for x in xrange(0, 1000):
        for y in xrange(0, 1000):
            if playground[x][y]:
                count +=1
    return count

dayFile = open("day6/input.txt", "r")
dayInput = dayFile.read().strip()