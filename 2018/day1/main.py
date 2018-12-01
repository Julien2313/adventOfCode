def p2():
    freq=0
    freqs={}
    while True:
        for data in dayInput.splitlines():
            freq += int(data)
            if freq in freqs:
                return freq
            else:
                freqs[freq] = 1


def p1():
    freq=0
    for data in dayInput.splitlines():
        freq += int(data)
    return freq

dayTxt = open("day1/input.txt", "r")
dayInput = dayTxt.read().strip()