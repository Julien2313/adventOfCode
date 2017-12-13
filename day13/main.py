def p1():
    firewalls = []
    picoSec = 0
    for firewall in day13Input.splitlines():
        depth, range = firewall.split(': ')
        firewalls.append([int(depth), int(range)])

    for firewall in firewalls:
        if firewall[0] % (2*(firewall[1]-1))==0:
            picoSec += firewall[1] * firewall[0]

    return picoSec

def p2():
    firewalls = []
    picoSecDelay = 0
    found = False
    for firewall in day13Input.splitlines():
        depth, range = firewall.split(': ')
        firewalls.append([int(depth), int(range)])

    while not found:
        found = True
        for firewall in firewalls:
            if (firewall[0] + picoSecDelay) % (2*(firewall[1]-1)) == 0:
                    found = False
                    picoSecDelay += 1
                    break
    return picoSecDelay

day13Input = open("day13/input.txt", "r").read().strip()
