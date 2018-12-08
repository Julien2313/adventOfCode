# stats : start 10:27
# 10h49
# 10h49

import hashlib

def p2():
    cpt = 0    
    while True:
        if "000000" == hashlib.md5(dayInput+str(cpt)).hexdigest()[:6]:
            return cpt
        cpt+=1

def p1():
    cpt = 0
    while True:
        if "00000" == hashlib.md5(dayInput+str(cpt)).hexdigest()[:5]:
            return cpt
        cpt+=1

dayFile = open("day4/input.txt", "r")
dayInput = dayFile.read().strip()