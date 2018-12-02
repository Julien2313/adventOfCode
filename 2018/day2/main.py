import sys
from collections import Counter

def p2():
    cptLine=0
    for line in dayInput.splitlines():
        cptLine+=1
        for line2 in dayInput.splitlines()[cptLine:]:
            diffs = zip(line, line2)
            cpt=0
            for char1, char2 in diffs:
                if char1 != char2:
                    cpt+=1
            if cpt == 1:
                txt=""
                for char1, char2 in diffs:
                    if char1 == char2:
                        txt+=char1
                return txt
                
def p1():
    cpt2 = 0
    cpt3 = 0
    for line in dayInput.splitlines():
        count = Counter(line)
        if 2 in count.values():
            cpt2+=1
        if 3 in count.values():
            cpt3+=1
    return cpt2*cpt3
    
dayFile = open("day2/input.txt", "r")
dayInput = dayFile.read().strip()