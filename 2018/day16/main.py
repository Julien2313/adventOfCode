import re

def addr(command, registers):
    registers[command[3]] = registers[command[1]] + registers[command[2]]
    return registers
def addi(command, registers):
    registers[command[3]] = registers[command[1]] + command[2]
    return registers
def mulr(command, registers):
    registers[command[3]] = registers[command[1]] * registers[command[2]]
    return registers
def muli(command, registers):
    registers[command[3]] = registers[command[1]] * command[2]
    return registers
def banr(command, registers):
    registers[command[3]] = registers[command[1]] & registers[command[2]]
    return registers
def bani(command, registers):
    registers[command[3]] = registers[command[1]] & command[2]
    return registers
def borr(command, registers):
    registers[command[3]] = registers[command[1]] | registers[command[2]]
    return registers
def bori(command, registers):
    registers[command[3]] = registers[command[1]] | command[2]
    return registers
def setr(command, registers):
    registers[command[3]] = registers[command[1]]
    return registers
def seti(command, registers):
    registers[command[3]] = command[1]
    return registers
def gtir(command, registers):
    if command[1] > registers[command[2]]:
        registers[command[3]] = 1
    else:
        registers[command[3]] = 0

    return registers
def gtri(command, registers):
    if registers[command[1]] > command[2]:
        registers[command[3]] = 1
    else:
        registers[command[3]] = 0

    return registers
def gtrr(command, registers):
    if registers[command[1]] > registers[command[2]]:
        registers[command[3]] = 1
    else:
        registers[command[3]] = 0
    return registers
def eqir(command, registers):
    if command[1] == registers[command[2]]:
        registers[command[3]] = 1
    else:
        registers[command[3]] = 0

    return registers
def eqri(command, registers):
    if registers[command[1]] == command[2]:
        registers[command[3]] = 1
    else:
        registers[command[3]] = 0

    return registers
def eqrr(command, registers):
    if registers[command[1]] == registers[command[2]]:
        registers[command[3]] = 1
    else:
        registers[command[3]] = 0
    return registers


def p2():
    registers = [0, 0, 0, 0]
    opcodes = [[True for x in xrange(16)] for y in xrange(16)]
    funcs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    firstPart = dayInput.split("\n\n\n")[0]
    secondPart = dayInput.split("\n\n\n")[1][1:]
    for lines in firstPart.split("\n\n"):
        before, commandStr, after = lines.splitlines()
        registersBefore = map(int, re.findall(r'\d+', before))
        command = map(int, re.findall(r'\d+', commandStr))
        RegistersAfter = map(int, re.findall(r'\d+', after))
        for func in xrange(len(funcs)):
            registerBis = funcs[func](command, registersBefore[:])
            if registerBis != RegistersAfter:
                opcodes[command[0]][func] = False

    for _ in xrange(16):
        for opcode in xrange(len(opcodes)):
            if opcodes[opcode].count(True) == 1:
                prio = opcodes[opcode].index(True)
                for opcode2 in xrange(len(opcodes)):
                    if opcode == opcode2:
                        continue
                    opcodes[opcode2][prio] = False
    for line in secondPart.splitlines():
        command = map(int, re.findall(r'\d+', line))
        funcs[opcodes[command[0]].index(True)](command, registers)


    return registers[0]

def p1():
    funcs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    firstPart = dayInput.split("\n\n\n")[0]
    cpt = 0
    for lines in firstPart.split("\n\n"):
        before, commandStr, after = lines.splitlines()
        registersBefore = map(int, re.findall(r'\d+', before))
        command = map(int, re.findall(r'\d+', commandStr))
        RegistersAfter = map(int, re.findall(r'\d+', after))
        cptOK = 0
        for func in funcs:
            registerBis = func(command, registersBefore[:])
            if registerBis == RegistersAfter:
                cptOK += 1
        if cptOK >= 3:
            cpt +=1
    return cpt


dayFile = open("day16/input.txt", "r")
dayInput = dayFile.read().strip()