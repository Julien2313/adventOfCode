
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


def p1_():
    x = y = 0.0
    for step in day11Input.split(','):
        if  step == "n":
            y += 1
        elif step == "s":
            y -= 1
        elif step == "nw":
            x += 0.5
            y -= 0.5
        elif step == "sw":
            x -= 0.5
            y -= 0.5
        elif step == "ne":
            x += 0.5
            y += 0.5
        elif step == "se":
            x -= 0.5
            y += 0.5

    return abs(x + y)

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
