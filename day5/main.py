
tab = chaine.splitlines()
index = 0
cpt = 0

while True:
    cpt = cpt + 1
    nextIndex = int(tab[index]) + index

    if int(tab[index]) >= 3:
        tab[index] = int(tab[index]) - 1
    else:
        tab[index] = int(tab[index]) + 1

    index = nextIndex
    if index >= len(tab):
        break
print cpt
