# stats : start 9h56
# 10h
# 10h11

def p2():
    totalSquareFeet=0
    for data in dayInput.splitlines():
        (x, y, z) = map(int,data.split("x"))

        
        totalSquareFeet += sum(sorted([x, y, z])[:2])*2 

        totalSquareFeet += x*y*z
    return totalSquareFeet

def p1():
    totalSquareFeet=0
    for data in dayInput.splitlines():
        (x, y, z) = map(int,data.split("x"))
        # print x, y, z
        totalSquareFeet += (2*x*y+2*y*z+2*z*x)
        totalSquareFeet += min([x*y, x*z, y*z])
    return totalSquareFeet

dayFile = open("day2/input.txt", "r")
dayInput = dayFile.read().strip()