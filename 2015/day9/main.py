# stats : start 12h27
# 12h25
import re
from collections import defaultdict

def p2():
    cpt = 0

def recur(citiesLeft):
    path = []
    if len(citiesLeft) == 1:
        return citiesLeft[0]

    for city in citiesLeft:
        print citiesLeft, city
        citiesMod  = citiesLeft[:]
        citiesMod.remove(city)
        print citiesLeft, citiesMod
        path.append(recur(citiesMod))
        print citiesLeft, path
    return path

def p1():
    distances = defaultdict(int)
    cities = []
    for line in dayInput.splitlines():
        city1, rest = line.split(" to ")
        city2, dist = rest.split(" = ")
        if city1 == min(city1, city2):
            distances[(city1, city2)] = int(dist)
        else:
            distances[(city2, city1)] = int(dist)
        if not city1 in cities:
            cities.append(city1)
        if not city2 in cities:
            cities.append(city2)

    print recur(cities)


dayFile = open("day9/input.txt", "r")
dayInput = dayFile.read().strip()