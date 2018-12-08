# stats : start 20h40
# 20h22
# 20h40

import re
from collections import defaultdict
import numpy as np

def p2():
    playground = [[0 for x in xrange(0, 1000)]for y in xrange(0, 1000)]

def getValue(wire):


def p1():
    wires = defaultdict(bytes)
    for line in dayInput.splitlines():
        compute, wireEnd = line.split(" -> ")
        print compute, wireEnd

        if "NOT" in compute:
            wires[wireEnd] = ~wires[compute.split(" ")[1]]
        elif "AND" in compute:
            wires[wireEnd] = wires[compute.split(" ")[0]] &  wires[compute.split(" ")[2]]
        elif "OR" in compute:
            wires[wireEnd] = wires[compute.split(" ")[0]] |  wires[compute.split(" ")[2]]
        elif "LSHIFT" in compute:
            wires[wireEnd] = np.left_shift(np.uint8(wires[compute.split(" ")[0]]), int(compute.split(" ")[2]))
        elif "RSHIFT" in compute:
            wires[wireEnd] = np.left_shift(np.uint8(wires[compute.split(" ")[0]]), int(compute.split(" ")[2]))
        else:
            wires[wireEnd] = int(compute)
    return wires["a"]


dayFile = open("day7/input.txt", "r")
dayInput = dayFile.read().strip()