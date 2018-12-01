def p2():
    freq=0
    freqs={freq}
    while True:
        for data in dayInput.splitlines():
            freq += int(data)
            if freq in freqs:
                return freq
            else:
                freqs.add(freq)

def p1():
    freq=0
    for data in dayInput.splitlines():
        freq += int(data)
    return freq

dayTxt = open("day1/input.txt", "r")
dayInput = dayTxt.read().strip()