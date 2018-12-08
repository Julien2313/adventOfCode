# stats : start 10:53
# 11h07
# 11h31

from collections import Counter
from collections import defaultdict

def p2():
    nice=0
    for line in dayInput.splitlines():
        if not any([True for letter in xrange(len(line)-2) if line[letter] == line[letter+2]]):
            continue

        if not any([True for letters in xrange(len(line)-1) if line[letters] + line[letters+1] in line[letters+2:]]):
            continue
        nice+=1

    return nice  

def p1():
    nice=0
    vowels = "aeiou"
    badWords = ["ab","cd","pq","xy"]
    for line in dayInput.splitlines():
        letters = Counter(line)
        if not sum([letters[vowel] for vowel in vowels if vowel in letters]) >= 3:
            continue
        if not any([True for letter in xrange(len(line)-1) if line[letter] == line[letter+1]]):
            continue
        if any([True for badWord in badWords if badWord in line]):
            continue
        nice+=1

    return nice


dayFile = open("day5/input.txt", "r")
dayInput = dayFile.read().strip()