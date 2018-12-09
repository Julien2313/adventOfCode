import re
from collections import deque

def p2():
    nbrPlayers, price = map(int, re.findall(r'\d+', dayInput))
    price *= 100
    scores = [0 for x in range(0, nbrPlayers)]
    playground = deque([0])
    player = lastPos = 0

    for marble in range(1, price + 1):
        if marble % 23 == 0:
            lastPos = (lastPos - 7) % len(playground)
            playground.rotate(-lastPos)
            scores[player] += marble
            scores[player] += playground.popleft()
            playground.rotate(lastPos + 6)
        else:
            playground.append(marble)
            playground.rotate(-1)

        lastPos = len(playground) - 2
        player = (player + 1) % nbrPlayers

    return max(scores)

def p1():
    nbrPlayers, price = map(int, re.findall(r'\d+', dayInput))

    playground = [0]
    scores = [0 for x in range(0, nbrPlayers)]
    lastPos = 0
    player = 0
    for marble in range(1, price + 1):
        if marble % 23 == 0:
            scores[player] += marble
            scores[player] += playground[(lastPos-7) % len(playground)]
            lastPos = (lastPos-7) % len(playground)
            del playground[lastPos:lastPos+1]
        else:
            lastPos = (lastPos+1) % (len(playground))+1
            playground[lastPos:lastPos] = [marble]

        player = (player + 1) % nbrPlayers

    return max(scores)

dayFile = open("day9/input.txt", "r")
dayInput = dayFile.read().strip()
