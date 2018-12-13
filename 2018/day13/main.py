from collections import defaultdict

def p2():
    carts = []
    crashed = []
    road = defaultdict(str)
    y = 0
    ID = 0
    for line in dayInput.splitlines():
        x = 0
        for char in line:
            if char == "<" or char == ">" or char == "^" or char == "v":
                carts.append([y, x, char, 0, ID])
                ID += 1
                if char == "<" or char == ">":
                    char = "-"
                else:
                    char = "|"
                
            road[(x, y)] = char
            x += 1
        y += 1
    # for y in xrange(150):
    #     print ''.join([road[(x, y)] for x in xrange(150)])

    while True:
        for cart in carts:
            if cart in crashed:
                continue
            
            if cart[2] == ">":
                cart[1]+=1
            elif cart[2] == "<":
                cart[1]-=1
            elif cart[2] == "v":
                cart[0]+=1
            elif cart[2] == "^":
                cart[0]-=1

            if road[(cart[1], cart[0])] == "+":
                if cart[3] % 3 == 0:
                    if cart[2] == ">":
                        cart[2] = "^"
                    elif cart[2] == "<":
                        cart[2] = "v"
                    elif cart[2] == "v":
                        cart[2] = ">"
                    elif cart[2] == "^":
                        cart[2] = "<"

                if cart[3] % 3 == 2:
                    if cart[2] == ">":
                        cart[2] = "v"
                    elif cart[2] == "<":
                        cart[2] = "^"
                    elif cart[2] == "v":
                        cart[2] = "<"
                    elif cart[2] == "^":
                        cart[2] = ">"
                cart[3] += 1
            elif road[(cart[1], cart[0])] == "\\" or road[(cart[1], cart[0])] == "/":
                if cart[2] == ">":
                    if road[(cart[1], cart[0])] == "\\":
                        cart[2] = "v"
                    else:
                        cart[2] = "^"
                elif cart[2] == "<":
                    if road[(cart[1], cart[0])] == "\\":
                        cart[2] = "^"
                    else:
                        cart[2] = "v"
                elif cart[2] == "^":
                    if road[(cart[1], cart[0])] == "\\":
                        cart[2] = "<"
                    else:
                        cart[2] = ">"
                elif cart[2] == "v":
                    if road[(cart[1], cart[0])] == "\\":
                        cart[2] = ">"
                    else:
                        cart[2] = "<"

            for cart2 in carts:
                if cart2 in crashed:
                    continue
                if cart2 == cart:
                    continue
                if cart[0] == cart2[0] and cart[1] == cart2[1]:# and cart[2] != cart2[2]:
                    crashed.append(cart)
                    crashed.append(cart2)
                    break
        carts.sort()
        if len(carts) - len(crashed) == 1:
            for cart in carts:
                if cart in crashed:
                    continue
                return str(cart[1])+","+str(cart[0])

def p1():
    carts = []
    road = defaultdict(str)
    y = 0
    for line in dayInput.splitlines():
        x = 0
        for char in line:
            if char == "<" or char == ">" or char == "^" or char == "v":
                carts.append([y, x, char, 0])
                if char == "<" or char == ">":
                    char = "-"
                else:
                    char = "|"
                
            road[(x, y)] = char
            x += 1
        y += 1
        
    while True:
        for cart in carts:
            if cart[2] == ">":
                cart[1]+=1
            elif cart[2] == "<":
                cart[1]-=1
            elif cart[2] == "v":
                cart[0]+=1
            elif cart[2] == "^":
                cart[0]-=1

            if road[(cart[1], cart[0])] == "+":
                if cart[3] % 3 == 0:
                    if cart[2] == ">":
                        cart[2] = "^"
                    elif cart[2] == "<":
                        cart[2] = "v"
                    elif cart[2] == "v":
                        cart[2] = ">"
                    elif cart[2] == "^":
                        cart[2] = "<"

                if cart[3] % 3 == 2:
                    if cart[2] == ">":
                        cart[2] = "v"
                    elif cart[2] == "<":
                        cart[2] = "^"
                    elif cart[2] == "v":
                        cart[2] = "<"
                    elif cart[2] == "^":
                        cart[2] = ">"
                cart[3] += 1

            elif road[(cart[1], cart[0])] == "\\" or road[(cart[1], cart[0])] == "/":
                if cart[2] == ">":
                    if road[(cart[1], cart[0])] == "\\":
                        cart[2] = "v"
                    else:
                        cart[2] = "^"
                elif cart[2] == "<":
                    if road[(cart[1], cart[0])] == "\\":
                        cart[2] = "^"
                    else:
                        cart[2] = "v"
                elif cart[2] == "^":
                    if road[(cart[1], cart[0])] == "\\":
                        cart[2] = "<"
                    else:
                        cart[2] = ">"
                elif cart[2] == "v":
                    if road[(cart[1], cart[0])] == "\\":
                        cart[2] = ">"
                    else:
                        cart[2] = "<"

            for cart2 in carts:
                if cart2 == cart:
                    continue
                if cart[0] == cart2[0] and cart[1] == cart2[1]:
                    return str(cart[1])+","+str(cart[0])
        carts.sort()

dayFile = open("day13/input.txt", "r")
dayInput = dayFile.read()
