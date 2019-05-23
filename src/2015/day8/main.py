# stats : start 12h07
# 12h25
def p2():
    cpt = 0
    for line in dayInput.splitlines():
        cpt += line.count('\\') + line.count('"')
        cpt += 2
    return cpt

def p1():
    cpt = 0
    for line in dayInput.splitlines():
        cpt += len(line) - len(eval(line))
    return cpt

dayFile = open("day8/input.txt", "r")
dayInput = dayFile.read().strip()