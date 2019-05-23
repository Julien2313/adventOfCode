import sys

def p2():
    dicRegister = {}
    tabInstructs = []
    maxi = -sys.maxint - 1
    for insctructions in day8Input.splitlines():
        tabInstruct = []
        for insctruction in insctructions.split(' '):
            tabInstruct.append(insctruction)
        tabInstructs.append(tabInstruct)
    for insctruction in tabInstructs:
        registerToModify = insctruction[0]
        value = int(insctruction[2])
        registerToCheck = insctruction[4]
        operator = insctruction[5]
        valueToCheck = int(insctruction[6])

        if insctruction[1] == "dec":
            value = value * -1

        if not registerToModify in dicRegister.keys():
            dicRegister[registerToModify] = 0
        if not registerToCheck in dicRegister.keys():
            dicRegister[registerToCheck] = 0

        if operator == ">":
            if dicRegister[registerToCheck] > valueToCheck:
                dicRegister[registerToModify] = dicRegister[registerToModify] + value
        elif operator == ">=":
            if dicRegister[registerToCheck] >= valueToCheck:
                dicRegister[registerToModify] = dicRegister[registerToModify] + value
        elif operator == "<":
            if dicRegister[registerToCheck] < valueToCheck:
                dicRegister[registerToModify] = dicRegister[registerToModify] + value
        elif operator == "<=":
            if dicRegister[registerToCheck] <= valueToCheck:
                dicRegister[registerToModify] = dicRegister[registerToModify] + value
        elif operator == "==":
            if dicRegister[registerToCheck] == valueToCheck:
                dicRegister[registerToModify] = dicRegister[registerToModify] + value
        else: #!=
            if dicRegister[registerToCheck] <> valueToCheck:
                dicRegister[registerToModify] = dicRegister[registerToModify] + value
        for value in dicRegister.items():
            if maxi < value[1]:
                maxi = value[1]

    return maxi

def p1():
    dicRegister = {}
    tabInstructs = []
    maxi = -sys.maxint - 1
    for insctructions in day8Input.splitlines():
        tabInstruct = []
        for insctruction in insctructions.split(' '):
            tabInstruct.append(insctruction)
        tabInstructs.append(tabInstruct)
    for insctruction in tabInstructs:
        registerToModify = insctruction[0]
        value = int(insctruction[2])
        registerToCheck = insctruction[4]
        operator = insctruction[5]
        valueToCheck = int(insctruction[6])

        if insctruction[1] == "dec":
            value = value * -1

        if not registerToModify in dicRegister.keys():
            dicRegister[registerToModify] = 0
        if not registerToCheck in dicRegister.keys():
            dicRegister[registerToCheck] = 0

        if operator == ">":
            if dicRegister[registerToCheck] > valueToCheck:
                dicRegister[registerToModify] = dicRegister[registerToModify] + value
        elif operator == ">=":
            if dicRegister[registerToCheck] >= valueToCheck:
                dicRegister[registerToModify] = dicRegister[registerToModify] + value
        elif operator == "<":
            if dicRegister[registerToCheck] < valueToCheck:
                dicRegister[registerToModify] = dicRegister[registerToModify] + value
        elif operator == "<=":
            if dicRegister[registerToCheck] <= valueToCheck:
                dicRegister[registerToModify] = dicRegister[registerToModify] + value
        elif operator == "==":
            if dicRegister[registerToCheck] == valueToCheck:
                dicRegister[registerToModify] = dicRegister[registerToModify] + value
        else: #!=
            if dicRegister[registerToCheck] <> valueToCheck:
                dicRegister[registerToModify] = dicRegister[registerToModify] + value
    for value in dicRegister.items():
        if maxi < value[1]:
            maxi = value[1]

    return maxi

day8Input = open("day8/input.txt", "r").read()