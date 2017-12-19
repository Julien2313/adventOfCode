def p1():
  registers = {}
  x = 0
  while x < len(day18Input.splitlines()) or x < 0:
    command = day18Input.splitlines()[x]
    data = command.split()
    #print data, x
    try:
      int(data[1])
    except ValueError:
      if not data[1] in registers:
        registers[data[1]] = 0
        
    if len(data) > 2:
      try:
        int(data[2])
      except ValueError:
        if not data[2] in registers:
          registers[data[2]] = 0
        
    if data[0] == "set":
      try:
        registers[data[1]] = int(data[2])
      except ValueError:
        registers[data[1]] = registers[data[2]]
    if data[0] == "add":
  		try:
  			registers[data[1]] += int(data[2])
  		except ValueError:
  			registers[data[1]] += registers[data[2]]
    if data[0] == "mul":
  		try:
  			registers[data[1]] *= int(data[2])
  		except ValueError:
  			registers[data[1]] *= registers[data[2]]
    if data[0] == "mod":
  		try:
  			registers[data[1]] %= int(data[2])
  		except ValueError:
  			registers[data[1]] %= registers[data[2]]
    if data[0] == "snd":
      snd = registers[data[1]]
    if data[0] == "rcv":
      return snd
      try:
        valReg = int(data[1])
      except ValueError:
        valReg = registers[data[1]]
      if valReg <> 0:
        registers[data[1]] = snd
  
    if data[0] == "jgz":
      try:
        valReg = int(data[1])
      except ValueError:
        valReg = registers[data[1]]
      if valReg > 0:
        try:
            x += int(data[2])
        except ValueError:
            x += registers[data[2]]
      else:
        x += 1
    else:
        x += 1



def p2():
  nbrProgs = 2
  cptSendProg1 = 0
  
  registers = []
  listSndToX = []
  cpts = []
  
  for prog in xrange(0, nbrProgs):
    registers.append({})
    listSndToX.append([])
    cpts.append(0)
  
  while True:
    cptsOK = False
    for numProg in xrange(0, nbrProgs):
      while cpts[numProg] <= 0 or cpts[numProg] < len(day18Input.splitlines()):
        cptsOK = True
        command = day18Input.splitlines()[cpts[numProg]]
        data = command.split()
        
        try:
          int(data[1])
        except ValueError:
          if not data[1] in registers[numProg]:
            registers[numProg][data[1]] = numProg
            
        if len(data) > 2:
          try:
            int(data[2])
          except ValueError:
            if not data[2] in registers[numProg]:
              registers[numProg][data[2]] = numProg
              
        if data[0] == "set":
          try:
            registers[numProg][data[1]] = int(data[2])
          except ValueError:
            registers[numProg][data[1]] = registers[numProg][data[2]]
        elif data[0] == "add":
          try:
            registers[numProg][data[1]] += int(data[2])
          except ValueError:
            registers[numProg][data[1]] += registers[numProg][data[2]]
        elif data[0] == "mul":
          try:
            registers[numProg][data[1]] *= int(data[2])
          except ValueError:
            registers[numProg][data[1]] *= registers[numProg][data[2]]
        elif data[0] == "mod":
          try:
            registers[numProg][data[1]] %= int(data[2])
          except ValueError:
            registers[numProg][data[1]] %= registers[numProg][data[2]]
        elif data[0] == "snd":
          try:
            listSndToX[(numProg + 1)%nbrProgs].append(int(data[1]))
          except ValueError:
            listSndToX[(numProg + 1)%nbrProgs].append(registers[numProg][data[1]])
          if numProg == 1:
            cptSendProg1 += 1
        elif data[0] == "rcv":
          if len(listSndToX[numProg]) == 0:
            break
          registers[numProg][data[1]] = listSndToX[numProg][0]
          listSndToX[numProg] = listSndToX[numProg][1:]
      
        if data[0] == "jgz":
          try:
            valReg = int(data[1])
          except ValueError:
            valReg = registers[numProg][data[1]]
          if valReg > 0:
            try:
              cpts[numProg] += int(data[2])
            except ValueError:
              cpts[numProg] += registers[numProg][data[2]]
          else:
            cpts[numProg] += 1
        else:
          cpts[numProg] += 1
      
    
    sndsOK = False
    
    for cpt in xrange(0, nbrProgs):
      if len(listSndToX[cpt]) <> 0:
        sndsOK = True
        break
        
    if not sndsOK:
      return cptSendProg1
      
    if not cptsOK:
      return cptSendProg1
      
  return cptSendProg1


day18Input = open("day18/input.txt", "r").read().strip()

