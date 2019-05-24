def p1():
    freq=0
    for data in dayInput.splitlines():
        freq += int(data)
    return freq

def p2():
    freq=0
    freqs=set([freq])
    while True:
        for data in dayInput.splitlines():
            freq += int(data)
            if freq in freqs:
                return freq
            freqs.add(freq)

dayFile = open("src/aoc2018/day1/input.txt", "r")
dayInput = dayFile.read().strip()