import re

def seti(a, b, c, registers):
    registers[c] = a

def setr(a, b, c, registers):
    registers[c] = registers[a]
    
def addi(a, b, c, registers):
    registers[c] = registers[a] + b
    
def addr(a, b, c, registers):
    registers[c] = registers[a] + registers[b]

def mulr(a, b, c, registers):
    registers[c] = registers[a] * registers[b]

def eqrr(a, b, c, registers):
    if registers[a] == registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0

def gtrr(a, b, c, registers):
    if registers[a] > registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0

def muli(a, b, c, registers):
    registers[c] = registers[a] * b
    
def p2():
    funcs = {"addr": addr, "addi": addi, "setr": setr, "seti": seti, "mulr": mulr, "eqrr": eqrr, "gtrr": gtrr, "muli": muli}

    ipReg = int(dayInput.splitlines()[0].split(" ")[1])
    commands = []
    for line in dayInput.splitlines()[1:]:
        command = line.split(" ")[0]
        a, b, c = map(int, re.findall(r'\d+', line))
        commands.append((command, a, b, c))
    
    registers = [0 for _ in xrange(6)]
    registers[0] = 1

    while 0 <= registers[ipReg] < len(commands):
        command, a, b, c = commands[registers[ipReg]]

        funcs[command](a, b, c, registers)
        
        registers[ipReg] += 1


    return registers[0]
    

def p1():
    funcs = {"addr": addr, "addi": addi, "setr": setr, "seti": seti, "mulr": mulr, "eqrr": eqrr, "gtrr": gtrr, "muli": muli}

    ipReg = int(dayInput.splitlines()[0].split(" ")[1])
    commands = []
    for line in dayInput.splitlines()[1:]:
        command = line.split(" ")[0]
        a, b, c = map(int, re.findall(r'\d+', line))
        commands.append((command, a, b, c))
    
    registers = [0 for _ in xrange(6)]

    while 0 <= registers[ipReg] < len(commands):
        command, a, b, c = commands[registers[ipReg]]

        funcs[command](a, b, c, registers)
        
        registers[ipReg] += 1


    return registers[0]
    


dayFile = open("day19/input.txt", "r")
dayInput = dayFile.read().strip()