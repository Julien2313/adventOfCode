def p2():
    tot = 0
    for line in day4Input.splitlines():
        tot = tot + 1
        words = line.split(' ')
        wordsChecked = []
        for wordRand in words:
            word = ''.join(sorted(wordRand))
            if word in wordsChecked:
                tot = tot - 1
                break
            else:
                wordsChecked.append(word)
    return tot

def p1():
    tot = 0
    for line in day4Input.splitlines():
        tot = tot + 1
        words = line.split(' ')
        wordsChecked = []
        for word in words:
            if word in wordsChecked:
                tot = tot - 1
                break
            else:
                wordsChecked.append(word)
    return tot

day4Input = open("day4/input.txt", "r").read()
