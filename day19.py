
def p1():
  word = ""
  pos = 1 + 0j
  dir = 0 + 1j
  
  land = day19Input.splitlines()
  
  while True:
    x = int(pos.real)
    y = int(pos.imag)
    if land[y][x] == " ":
      return word
    elif land[y][x].isalpha():
      word += land[y][x]
    elif land[y][x] == "+":
      dir *= 1j
      if dir.real == 0:
        sign = "|"
      else:
        sign = "-"  
      if land[int((pos + dir).imag)][int((pos + dir).real)] != sign and not land[int((pos + dir).imag)][int((pos + dir).real)].isalpha():
        dir *= -1
    pos += dir
  
  return -1

def p2():
  pos = 1 + 0j
  dir = 0 + 1j
  cpt = 0
  
  land = day19Input.splitlines()
  
  while True:
    x = int(pos.real)
    y = int(pos.imag)
    if land[y][x] == " ":
      return cpt
    elif land[y][x] == "+":
      dir *= 1j
      if dir.real == 0:
        sign = "|"
      else:
        sign = "-"  
      if land[int((pos + dir).imag)][int((pos + dir).real)] != sign and not land[int((pos + dir).imag)][int((pos + dir).real)].isalpha():
        dir *= -1
    pos += dir
    cpt += 1
  
  return -1


day19Input = open("day19/input.txt", "r").read().strip()
