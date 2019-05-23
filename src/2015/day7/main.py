import re
from collections import defaultdict
import sys

def recur(lines, wireToFind, wires):
    if wireToFind.isdigit():
        return int(wireToFind)
    if wireToFind in wires:
        return wires[wireToFind]

    for line in lines:
        compute, wireEnd = line.split(" -> ")
        if wireEnd == wireToFind:
            lines.remove(line)
            if "NOT" in compute:
                value = recur(lines, compute.split(" ")[1], wires)
                valueWire = ~value
            else:
                wire1 = compute.split(" ")[0]
                try:
                    wire2 = compute.split(" ")[2]
                    if "AND" in compute:
                        value1 = recur(lines, wire1, wires)
                        value2 = recur(lines, wire2, wires)
                        valueWire = value1 & value2
                    elif "OR" in compute:
                        value1 = recur(lines, wire1, wires)
                        value2 = recur(lines, wire2, wires)
                        valueWire = value1 |  value2
                    elif "LSHIFT" in compute:
                        value = recur(lines, wire1, wires)
                        valueWire = value <<  int(wire2)
                    elif "RSHIFT" in compute:
                        value = recur(lines, wire1, wires)
                        valueWire = value >>  int(wire2)
                except:
                    valueWire = recur(lines, wire1, wires)

            wires[wireToFind] = valueWire
            return valueWire
 

def p2():
    wires = defaultdict(int)
    wireA = recur(dayInput.splitlines(), "a", wires)
    wires = defaultdict(int)
    wires["b"] = wireA

    return recur(dayInput.splitlines(), "a", wires)


def p1():
    wires = defaultdict(int)
    return recur(dayInput.splitlines(), "a", wires)


dayFile = open("day7/input.txt", "r")
dayInput = dayFile.read().strip()