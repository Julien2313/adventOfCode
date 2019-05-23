def splitInt(number):
    if number >= 10:
        return divmod(number, 10)
    else:
        return (number,)

def p2():
    recipes = [3, 7]
    elfs = [0, 1]
    digits = [int(digit) for digit in str(dayInput)]

    while recipes[-len(digits):] != digits and recipes[-len(digits)-1:-1] != digits:
        totRecip = recipes[elfs[0]] + recipes[elfs[1]]
        recipes.extend(splitInt(totRecip))

        elfs = [(elfs[elf] + recipes[elfs[elf]] +1) % len(recipes) for elf in xrange(len(elfs))]

    return len(recipes) - len(digits) - (0 if recipes[-len(digits):] == digits else 1)

def p1():
    recipes = [3, 7]
    elfs = [0, 1]

    while len(recipes) < int(dayInput) + 10:
        totRecip = recipes[elfs[0]] + recipes[elfs[1]]
        recipes.extend(splitInt(totRecip))

        elfs = [(elfs[elf] + recipes[elfs[elf]] +1) % len(recipes) for elf in xrange(len(elfs))]

    return ''.join(str(recipe) for recipe in recipes[int(dayInput):int(dayInput)+10])

dayFile = open("day14/input.txt", "r")
dayInput = dayFile.read()
