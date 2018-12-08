# stats : start 9h51
# 9h53
# 9h55

def p2():
    floor=0
    pos=1
    for data in dayInput:
        if data == '(':
            floor+=1
        else:
            floor-=1
        if floor == -1:
            return pos
        pos+=1
    return floor

def p1():
    floor=0
    for data in dayInput:
        if data == '(':
            floor+=1
        else:
            floor-=1
    return floor

dayFile = open("day1/input.txt", "r")
dayInput = dayFile.read().strip()