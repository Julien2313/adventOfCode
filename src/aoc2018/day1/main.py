def p2():
    freq=0
    freqs=set([freq])
    while True:
        for data in dayInput.splitlines():
            freq += int(data)
            if freq in freqs:
                return freq
            freqs.add(freq)

def p1():
    freq=0
    for data in dayInput.splitlines():
        freq += int(data)
    return freq

dayFile = open("day1/input.txt", "r")
dayInput = dayFile.read().strip()