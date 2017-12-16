def AG():
    valueA = 634
    while True:
        valueA =  (valueA * 16807) % 2147483647
        yield valueA

def BG():
    valueB = 301
    while True:
        valueB =  (valueB * 48271) % 2147483647
        yield valueB

def AG_():
    valueA = 634
    while True:
        valueA =  (valueA * 16807) % 2147483647
        if valueA % 4 == 0:
            yield valueA

def BG_():
    valueB = 301
    while True:
        valueB =  (valueB * 48271) % 2147483647
        if valueB % 8 == 0:
            yield valueB


def p1():
    VALUE_MASK = 0xffff
    A = AG()
    B = BG()
    cpt = 0
    for x in range(40000000):
        valueA = next(A)
        valueB = next(B)
        if (VALUE_MASK & valueA) == (VALUE_MASK & valueB):
            cpt += 1
    return cpt

def p1_():
    VALUE_MASK = 0xffff
    generatorA = 634
    generatorB = 301
    cpt = 0

    for x in range(40000000):
        generatorA = (generatorA * 16807) % 2147483647
        generatorB = (generatorB * 48271) % 2147483647
        if (VALUE_MASK & generatorA) == (VALUE_MASK & generatorB):
            cpt += 1
    return cpt

def p2_():
    VALUE_MASK = 0xffff
    A = AG_()
    B = BG_()
    cpt = 0
    for x in range(5000000):
        valueA = next(A)
        valueB = next(B)
        if (VALUE_MASK & valueA) == (VALUE_MASK & valueB):
            cpt += 1

    return cpt


def p2():
    VALUE_MASK = 0xffff
    generatorA = 634
    generatorB = 301
    cpt = 0
    valuesA = []
    valuesB = []
    while min(len(valuesB), len(valuesA)) < 5000000:
        generatorA = (generatorA * 16807) % 2147483647
        generatorB = (generatorB * 48271) % 2147483647
        if generatorA % 4 == 0:
            valuesA.append(generatorA)
        if generatorB % 8 == 0:
            valuesB.append(generatorB)

    for x in range(min(len(valuesB), len(valuesA))):
        if (VALUE_MASK & valuesA[x]) == (VALUE_MASK & valuesB[x]):
            cpt += 1

    return cpt

day15Input = open("day15/input.txt", "r").read().strip()
