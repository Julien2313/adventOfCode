DAY3INPUT = 265149


def day3_ChangeDirection():
    
    day3_ChangeDirection.counter = (day3_ChangeDirection.counter + 1) % 4
    counter = day3_ChangeDirection.counter
    
    if counter == 0:#bas
        #~ print "bas"
        return (0, -1)        
    elif counter == 1:# droite
        #~ print "droite"
        return (1, 0)
    elif counter == 2:# haut
        #~ print "haut"
        return (0, 1)    
    else:# gauche
        #~ print "gauche"
        return (-1, 0)
            
day3_ChangeDirection.counter = 1

def p2(): #not done
    width = 1
    while True:
        if width * width >= DAY3INPUT:
            break
        else:
            width += 2
    width += 2

    matrix = [[0 for x in xrange(0, width)] for y in xrange(0, width)]
    x, y = width/2, width/2
    deltaX = 0
    deltaY = 0
    matrix[x][y] = 1
    x += 1
    
    cpt = 1
    while cpt < 10:
        for twoTimes in xrange(0, 2):
            for cptTimes in xrange(0, cpt):
                matrix[x][y] = matrix[x+1][y] + matrix[x+1][y+1] + matrix[x-1][y+1] + matrix[x-1][y-1] + matrix[x][y-1] + matrix[x][y+1] + matrix[x-1][y] + matrix[x+1][y-1]

                    
                if matrix[x][y] > DAY3INPUT:
                    return matrix[x][y]
                x += deltaX
                y += deltaY
                    
            deltaX, deltaY = day3_ChangeDirection()
        cpt = cpt + 1


def p1():
    width = 1
    num = DAY3INPUT
    while True:
        if width * width >= num:
            break
        else:
            width = width + 2
    squareCpt = width * width

    #"put" the number on the last line
    num = num + (3 - (num - (width - 2) * (width - 2))/ (width)) * (width - 1)
    #       hauteur        + largeur
    return (width - 1) / 2 + abs(squareCpt - (width - 1) / 2 - num)

