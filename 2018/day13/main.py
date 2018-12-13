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
            pos = x*1j+ y
            if char in "<>^v":
                if char == "<":
                    dir = -1j + 0
                elif char == "^":
                    dir = 0j - 1
                elif char == ">":
                    dir = 1j + 0
                else:
                    dir = 0j + 1

                carts.append([pos, dir, 0, ID])
                if char in "<>":
                    char = "-"
                else:
                    char = "|"
                ID+=1
            
            road[pos] = char
            x += 1
        y += 1
        
    while True:
        # for y in xrange(150):
        #     print ''.join([road[x*1j+y] if not any([cart[0] == x*1j+y for cart in carts]) else "*" for x in xrange(150)])

        for cart in carts:
            if cart in crashed:
                continue
            cart[0] += cart[1]
            if road[cart[0]] == "+":
                if cart[2] % 3 == 0:
                    cart[1] *= 1j
                if cart[2] % 3 == 2:
                    cart[1] *= -1j
                cart[2] += 1
            elif road[cart[0]] == "\\":
                if cart[1].real != 0:
                    cart[1] *= 1j
                else:
                    cart[1] *= -1j
            elif road[cart[0]] == "/":
                if cart[1].real != 0:
                    cart[1] *= -1j
                else:
                    cart[1] *= 1j

            for cart2 in carts:
                if cart2 in crashed:
                    continue
                if cart2 == cart:
                    continue
                if cart[0] == cart2[0]:
                    crashed.append(cart)
                    crashed.append(cart2)
                    break

        carts.sort(key=lambda x:x[0].imag*1000+x[0].real)

        if len(carts) - len(crashed) == 1:
            for cart in carts:
                if cart in crashed:
                    continue
                return str(int(cart[0].imag))+","+str(int(cart[0].real))

def p1():
    carts = []
    road = defaultdict(str)
    y = 0
    ID = 0
    for line in dayInput.splitlines():
        x = 0
        for char in line:
            pos = x*1j+ y
            if char in "<>^v":
                if char == "<":
                    dir = -1j + 0
                elif char == "^":
                    dir = 0j - 1
                elif char == ">":
                    dir = 1j + 0
                else:
                    dir = 0j + 1

                carts.append([pos, dir, 0, ID])
                if char in "<>":
                    char = "-"
                else:
                    char = "|"
                ID+=1
            
            road[pos] = char
            x += 1
        y += 1
        
    while True:
        # for y in xrange(7):
        #     print ''.join([road[x*1j+y] if not any([cart[0] == x*1j+y for cart in carts]) else "*" for x in xrange(15)])
        for cart in carts:
            cart[0] += cart[1]

            if road[cart[0]] == "+":
                if cart[2] % 3 == 0:
                    cart[1] *= 1j
                if cart[2] % 3 == 2:
                    cart[1] *= -1j
                cart[2] += 1
            elif road[cart[0]] == "\\":
                if cart[1].real != 0:
                    cart[1] *= 1j
                else:
                    cart[1] *= -1j
            elif road[cart[0]] == "/":
                if cart[1].real != 0:
                    cart[1] *= -1j
                else:
                    cart[1] *= 1j

            for cart2 in carts:
                if cart2 == cart:
                    continue
                if cart[0] == cart2[0]:
                    return str(int(cart[0].imag))+","+str(int(cart[0].real))
        carts.sort(key=lambda x:x[0].imag*1000+x[0].real)

dayFile = open("day13/input.txt", "r")
dayInput = dayFile.read()
