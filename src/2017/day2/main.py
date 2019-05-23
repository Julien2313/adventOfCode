import sys

def p2():
    tot = 0
    oldTot = 0
    for line in day2Input.splitlines():
        numbers = line.split('\t')
        for i in xrange(0, len(numbers)):
            for j in xrange(i + 1, len(numbers)):
                n1 = int(numbers[i])
                n2 = int(numbers[j])
                if n1 % n2 == 0:
                    tot = tot + (n1 / n2)
                    break
                if n2 % n1 == 0:
                    tot = tot + (n2 / n1)
                    break
            if oldTot <> tot:
                oldTot = tot
                break
    return tot

def p1():
    tot = 0
    for line in day2Input.splitlines():
        max = 0
        min = sys.maxint
        for number in line.split('\t'):
            if max < int(number):
                max = int(number)
            if min > int(number):
                min = int(number)
        tot = tot + (max - min)
    return tot

day2Input = open("day2/input.txt", "r").read()