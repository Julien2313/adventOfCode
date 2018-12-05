from collections import Counter
from datetime import datetime
from operator import itemgetter
import operator
import time

january1st = datetime(1518, 01, 01)

def p2():
    lines=[]
    for line in dayInput.splitlines():
        datetime_object = datetime.strptime(line.split("] ")[0][1:], '%Y-%m-%d %H:%M')
        # print datetime_object
        string = line.split("] ")[1]
        lines.append([(datetime_object-january1st).total_seconds()/60, int(line[15:17]), string, int(line[12:14])])
        
    lines = sorted(lines, key=itemgetter(0))
    guards={}
    #guard
    #0: minutes
    #1: derniere fois que leve
    #2: total minutes
    currentGuard=0
    for line in lines:
        order  = line[2]
        minute = line[1]
        
        if "Guard" in order:
            currentGuard=order.split("#")[1].split(' ')[0]
            if not(currentGuard in guards):
                minutes = [0 for x in xrange(60)]
                guards[currentGuard] = [minutes, minute, 0]

        elif "falls" in order:
            guards[currentGuard][1] = minute
        #wake
        else:
            for minutes in xrange(guards[currentGuard][1], minute):
                guards[currentGuard][0][minutes] += 1
                guards[currentGuard][2] += 1

    guardMax=0
    maxFreq = 0
    for guard in guards:
        cpt = 0
        for minute in guards[guard][0]:
            if maxFreq < minute:
                maxCpt = cpt
                maxFreq = minute
                guardMax =guard 
            cpt+=1

    return int(guardMax) * maxCpt
    

def p1():
    lines=[]
    for line in dayInput.splitlines():
        datetime_object = datetime.strptime(line.split("] ")[0][1:], '%Y-%m-%d %H:%M')
        # print datetime_object
        string = line.split("] ")[1]
        lines.append([(datetime_object-january1st).total_seconds()/60, int(line[15:17]), string, int(line[12:14])])
        
    lines = sorted(lines, key=itemgetter(0))
    guards={}
    #guard
    #0: minutes
    #1: derniere fois que leve
    #2: total minutes
    currentGuard=0
    for line in lines:
        order  = line[2]
        minute = line[1]
        
        if "Guard" in order:
            currentGuard=order.split("#")[1].split(' ')[0]
            if not(currentGuard in guards):
                minutes = [0 for x in xrange(60)]
                guards[currentGuard] = [minutes, minute, 0]

        elif "falls" in order:
            guards[currentGuard][1] = minute
        #wake
        else:
            for minutes in xrange(guards[currentGuard][1], minute):
                guards[currentGuard][0][minutes] += 1
                guards[currentGuard][2] += 1

    max=0
    guardMax=0
    for guard in guards:
        if max < guards[guard][2]:
            max = guards[guard][2]
            guardMax = guard
    
    maxCpt = -1
    maxMinute = -1
    cpt = 0
    for minute in guards[guardMax][0]:
        if maxCpt < minute:
            maxCpt = minute
            maxMinute = cpt
        cpt+=1
    print int(guardMax), maxMinute
    return int(guardMax) * maxMinute

dayFile = open("day4/input.txt", "r")
dayInput = dayFile.read().strip()
