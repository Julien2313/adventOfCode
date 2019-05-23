from collections import defaultdict

def p2():
    allTasks = set()
    dependances = defaultdict(set)
    for line in dayInput.splitlines():
        stepA = line[5]
        stepB = line[36]
        dependances[stepB].add(stepA)
        allTasks.add(stepB)
        allTasks.add(stepA)
    
    tasksSorted = sorted(allTasks)

    heureFini = {}
    tempsUtilise = [0 for x in xrange(5)]
    stepsPrint = ''
    globalTimer = 0

    while len(tasksSorted) != 0:
        for t in tempsUtilise:
            if t <= globalTimer:
                break
        else:
            time = min(tempsUtilise)
        for task in tasksSorted:
            for taskDeps in dependances[task]:
                if not(taskDeps in heureFini and heureFini[taskDeps] <= globalTimer):
                    break
            else:
                stepsPrint += task
                for numTimer, _ in enumerate(tempsUtilise):
                    if tempsUtilise[numTimer] <= globalTimer:
                        tempsUtilise[numTimer] = globalTimer + 60 + ord(task) - ord('A') + 1 
                        heureFini[task] = tempsUtilise[numTimer]
                        break
                tasksSorted.remove(task)
                break
        else:
            # globalTimer = min(time for time in tempsUtilise if time > globalTimer)
            timers=[]
            for time in tempsUtilise:
                if time > globalTimer:
                    timers.append(time)
            globalTimer = min(timers)
  
    return max(tempsUtilise)

def p1():
    allTasks = set()
    dependances = defaultdict(set)
    for line in dayInput.splitlines():
        stepA = line[5]
        stepB = line[36]
        dependances[stepB].add(stepA)
        allTasks.add(stepB)
        allTasks.add(stepA)
    
    tasksSorted = sorted(allTasks)
    fait = set()
    toPrint = ''

    while len(tasksSorted) != 0:
        for task in tasksSorted:
            # if not (dependances[task] - fait):
            for taskDeps in dependances[task]:
                if not(taskDeps in fait):
                    break
            else:
                toPrint += task
                fait.add(task)
                tasksSorted.remove(task)
                break
    return toPrint

dayFile = open("day7/input.txt", "r")
dayInput = dayFile.read().strip()
