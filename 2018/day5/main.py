import string

def p2():
    best = 999999999
    data = dayInput
    while True:
        lenBefore = len(data)
        for x in string.ascii_lowercase[:26]:
            couple = x+x.upper()
            data = data.replace(couple, "")
            couple = x.upper()+x
            data = data.replace(couple, "")

        if lenBefore == len(data):
            lineShort = data
            break

    for x in string.ascii_lowercase[:26]:
        data = lineShort.replace(x, "").replace(x.upper(), "")
        while True:
            lenBefore = len(data)
            for x in string.ascii_lowercase[:26]:
                couple = x+x.upper()
                data = data.replace(couple, "")
                couple = x.upper()+x
                data = data.replace(couple, "")

            if lenBefore == len(data):
                if len(data) < best:
                    best=len(data)
                break
    return best

def p1():
    data = dayInput
    while True:
        lenBefore = len(data)
        for x in string.ascii_lowercase[:26]:
            couple = x+x.upper()
            data = data.replace(couple, "")
            couple = x.upper()+x
            data = data.replace(couple, "")

        if lenBefore == len(data):
            return len(data)

dayFile = open("day5/input.txt", "r")
dayInput = dayFile.read().strip()
