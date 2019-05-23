
def p2():
    x = y = z = 0
    distances = []
    for step in day11Input.split(','):
        if  step == "n":
            y += 1
            z -= 1
        elif step == "s":
            y -= 1
            z += 1
        elif step == "nw":
            y += 1
            x -= 1
        elif step == "sw":
            z += 1
            x -= 1
        elif step == "ne":
            z -= 1
            x += 1
        elif step == "se":
            y -= 1
            x += 1
        distances.append((abs(x) + abs(y) + abs(z)) / 2)
    return max(distances)

def p2_():
    positions = [0, 0, 0]
    distances = []
    directions = {'n':(0, 1, -1), 's':(0, -1, 1), 'nw':(-1, 1, 0), 'sw':(-1, 0, 1), 'ne':(1, 0, -1), 'se':(1, -1, 0)}
    for step in day11Input.split(','):
        pos = []
        [pos.append(x + y) for x, y in zip(positions, directions[step])]
        positions = list(pos)
        distances.append((abs(positions[0]) + abs(positions[1]) + abs(positions[2])) / 2)
    return max(distances)


def p1_():
    positions = [0, 0, 0]
    directions = {'n':(0, 1, -1), 's':(0, -1, 1), 'nw':(-1, 1, 0), 'sw':(-1, 0, 1), 'ne':(1, 0, -1), 'se':(1, -1, 0)}
    for step in day11Input.split(','):
        pos = []
        [pos.append(x + y) for x, y in zip(positions, directions[step])]
        positions = list(pos)
    return ((abs(positions[0]) + abs(positions[1]) + abs(positions[2])) / 2)

def p1():
    x = y = z = 0
    for step in day11Input.split(','):
        if  step == "n":
            y += 1
            z -= 1
        elif step == "s":
            y -= 1
            z += 1
        elif step == "nw":
            y += 1
            x -= 1
        elif step == "sw":
            z += 1
            x -= 1
        elif step == "ne":
            z -= 1
            x += 1
        elif step == "se":
            y -= 1
            x += 1

    return ((abs(x) + abs(y) + abs(z)) / 2)

day11Input = open("day11/input.txt", "r").read().strip()
