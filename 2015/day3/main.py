# stats : start 10:13
# 10h21
# 10h11
from collections import defaultdict
from collections import Counter

def p2():
    playground = defaultdict(int)
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    playground[(x1, y1)] += 1

    for data in zip(dayInput[::2], dayInput[1::2]):
        if data[0] == '>':
            y1+=1
        elif data[0] == '<':
            y1-=1
        elif data[0] == 'v':
            x1-=1
        else: 
            x1+=1
        playground[(x1, y1)] += 1
        
        if data[1] == '>':
            y2+=1
        elif data[1] == '<':
            y2-=1
        elif data[1] == 'v':
            x2-=1
        else: 
            x2+=1
        playground[(x2, y2)] += 1

    return sum([1 for x in Counter(playground).values()])

def p1():
    playground = defaultdict(int)
    x, y = 0, 0
    playground[(x, y)] += 1

    for data in dayInput:
        if data == '>':
            y+=1
        elif data == '<':
            y-=1
        elif data == 'v':
            x-=1
        else: 
            x+=1
        playground[(x, y)] += 1

    return sum([1 for x in Counter(playground).values()])

dayFile = open("day3/input.txt", "r")
dayInput = dayFile.read().strip()