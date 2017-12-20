
def p2():
  particules = []
  for x in day20Input.splitlines():
    x = x.split(', ')
    particule = []
    for vector in xrange(0, len(x)):
      particule.append(map(int, x[vector][3:-1].split(',')))
    particules.append(particule)
  z = 0
  while z < 5000:
    pos = []
    for x in xrange(0, len(particules)):
      particule = particules[x]
      particule[1][0] +=particule[2][0]
      particule[1][1] +=particule[2][1]
      particule[1][2] +=particule[2][2]
      
      particule[0][0] +=particule[1][0]
      particule[0][1] +=particule[1][1]
      particule[0][2] +=particule[1][2]

    collisions = []
    for particule1 in particules:
      for particule2 in particules:
        if particule2 == particule1:
          continue
        
        if particule1[0] == particule2[0]:
          if not particule1 in collisions:
            collisions.append(particule1)
          if not particule2 in collisions:
            collisions.append(particule2)
    
    for collision in collisions:
      particules.remove(collision)
      
    print len(particules)
       
    z += 1
      
    
def p1():
  particules = []
  for x in day20Input.splitlines():
    x = x.split(', ')
    particule = []
    for vector in xrange(0, len(x)):
      particule.append(map(int, x[vector][3:-1].split(',')))
    particules.append(particule)
    
  minAccel = 9999999
  for x in xrange(0, len(particules)):
    particule = particules[x]
     
    accel = pow(abs(particule[2][0]) + abs(particule[2][1]) + abs(particule[2][2]), 1.0/3)
    if accel < minAccel:
      minAccel = accel
      slower = x
  return slower
  
  

  
day20Input = open("day20/input.txt", "r").read()
