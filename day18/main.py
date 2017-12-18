
def p1():
    registers = {}
    registers2 = {}
    x = 0
    while x < len(day18Input.splitlines()):
        command = day18Input.splitlines()[x]
       # print command
        data = command.split()
        if len(data) > 2:
            if not data[2] in registers:
                data[2] = int(data[2])
            else:
                data[2] = registers[data[2]]
            if not data[2] in registers:
                registers[data[2]] = 0
        if not data[1] in registers:
            registers[data[1]] = 0

        if data[0] == "set":
            registers[data[1]] = data[2]
        if data[0] == "add":
            registers[data[1]] += data[2]
        if data[0] == "mul":
            registers[data[1]] *= data[2]
        if data[0] == "mod":
            registers[data[1]] %= data[2]
        if data[0] == "snd":
            registers2[data[1]] = registers[data[1]]
            print registers[data[1]]
        if data[0] == "rcv" and  registers[data[1]] <> 0:
            registers[data[1]] = registers2[data[1]]
        if data[0] == "jgz" and registers[data[1]] > 0:
            x += data[2]
        else:
            x += 1


        command = day18Input.splitlines()[x]
        # print command
        data = command.split()
        if len(data) > 2:
            if not data[2] in registers2:
                data[2] = int(data[2])
            else:
                data[2] = registers2[data[2]]
            if not data[2] in registers2:
                registers2[data[2]] = 1
        if not data[1] in registers2:
            registers2[data[1]] = 1

        if data[0] == "set":
            registers2[data[1]] = data[2]
        if data[0] == "add":
            registers2[data[1]] += data[2]
        if data[0] == "mul":
            registers2[data[1]] *= data[2]
        if data[0] == "mod":
            registers2[data[1]] %= data[2]
        if data[0] == "snd":
            registers[data[1]] = registers2[data[1]]
            print registers2[data[1]]
        if data[0] == "rcv" and registers2[data[1]] <> 0:
            registers2[data[1]] = registers[data[1]]
        if data[0] == "jgz" and registers2[data[1]] > 0:
            x += data[2]
        else:
            x += 1

        print registers, registers2


def p2():
    return 1


day18Input = open("day18/input.txt", "r").read().strip()
