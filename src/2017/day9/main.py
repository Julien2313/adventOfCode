day9_cpt = 0

def day9_RecurGarbage(day9Input, index):
    global day9_cpt
    while index < len(day9Input):
        if day9Input[index] != '!':
            if day9Input[index] == '>':
                return index
            index += 1
            day9_cpt += 1
        else:
            index += 2

def day9_Recur(day9Input, index, score):
    scoreEnfants = 0

    while index < len(day9Input):
        if day9Input[index] == '{':
            addScoreEnfants, index = day9_Recur(day9Input, index + 1, score + 1)
            scoreEnfants += addScoreEnfants
        if day9Input[index] == '}':
            return score + scoreEnfants, index + 1
        if day9Input[index] == '<':
            index = day9_RecurGarbage(day9Input, index + 1)
        index += 1

def p2():
    global day9_cpt
    day9_Recur(day9Input, 1, 1)[0]
    return day9_cpt

def day9RecurGarbage(day9Input, index):
    while index < len(day9Input):
        if day9Input[index] != '!':
            if day9Input[index] == '>':
                return index
            index += 1
        else:
            index += 2

def day9Recur(day9Input, index, score):
    scoreEnfants = 0

    while index < len(day9Input):
        if day9Input[index] == '{':
            addScoreEnfants, index = day9Recur(day9Input, index + 1, score + 1)
            scoreEnfants += addScoreEnfants
        if day9Input[index] == '}':
            return score + scoreEnfants, index+1
        if day9Input[index] == '<':
            index = day9RecurGarbage(day9Input, index + 1)
        index += 1

def p1():
    return day9Recur(day9Input, 1, 1)[0]

day9Input = open("day9/input.txt", "r").read()