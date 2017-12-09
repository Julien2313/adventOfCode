DAY6INPUT = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"

def p2():
    rayInput = DAY6INPUT
    input = []
    inputSow = []
    for number in rayInput.split('\t'):
        input.append(int(number))
    cycle = 0    
    
    while True:
        cycle = cycle + 1
        if input in inputSow:
            return cycle - 1 - inputSow.index(input)
        inputSow.append(list(input))

        maxi = max(input)
        indexMaxi = input.index(maxi)
        for number in xrange(0, min(maxi + 1, len(input))):
            index = (indexMaxi + number) % len(input)
            if input[index] == maxi:
                input[index] = input[index] - min(maxi, len(input) - 1)
                maxi = sys.maxint
            else:
                input[index] = input[index] + 1

def p1():
    rayInput = DAY6INPUT
    input = []
    inputSow = []
    for number in rayInput.split('\t'):
        input.append(int(number))
    cycle = 0    
    
    while True:
        cycle = cycle + 1
        if input in inputSow:
            return cycle - 1
        inputSow.append(list(input))

        maxi = max(input)
        indexMaxi = input.index(maxi)
        for number in xrange(0, min(maxi + 1, len(input))):
            index = (indexMaxi + number) % len(input)
            if input[index] == maxi:
                input[index] = input[index] - min(maxi, len(input) - 1)
                maxi = sys.maxint
            else:
                input[index] = input[index] + 1
