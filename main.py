#Diego Miguel M. Villamil
#CMSC 132 AB2L
#Exercise 9

import copy


#Reads instructions from given filename
def readIns(filename):
  instructions = []
  regs = ["R1","R2","R3","R4","R5",
          "R6","R7","R8","R9","R10",
          "R11","R12","R13","R14","R15"]

  fp = open(filename, "r")

  for line in fp:
    temp = line.strip()
    temp = temp.split(" ")
    temp[1] = temp[1].split(",")
    hasInvalidReg = False
    for reg in temp[1]:
      if(reg not in regs):#Check for invalid registers
        hasInvalidReg = True

    if(hasInvalidReg):
      print("input instructions contained invalid registers")
      return(None)

    temp.append([]) #[2]
    instructions.append(temp)

  return instructions

#Start of main
ins = readIns("input.in")
if(ins == None):
  exit()

pipeline = ['F','D','E','M','W']
time = 0

for i in range(0,len(ins)):
  if(i == 0):               #First instruction is always just F D E M W
    for E in pipeline:
      ins[i][2].append(E)
  else:
    j = 0
    if((ins[i - 1][2][j] == "-" ) or (ins[i - 1][2][j] == "F" ) or (ins[i - 1][2][j] == "S" )): #Add - while waiting for F to be available
      while((ins[i - 1][2][j] == "-" ) or (ins[i - 1][2][j] == "F" ) or (ins[i - 1][2][j] == "S" )):
        ins[i][2].append('-')
        if(j == (len(ins[i-1][2]) - 1)):
          break
        j += 1

    for E in pipeline:
      if(E == 'D'):
        for j in range((i-1),0,-1):
          prev = set(ins[j][2])
          curr = set(ins[i][2])
          if(len(prev & curr) > 0):
            diff = len(ins[j][2]) - len(ins[i][2])
            for k in range(0,diff):
              ins[i][2].append('S') #Add stalls while waiting for registers to not be used by previous instructions
      ins[i][2].append(E)
time += 1


for row in ins:               #Output result to terminal
  print(row[0], " ",end="")
  for reg in row[1]:
    if(row[1].index(reg) == (len(row[1]) - 1)):
      print(reg," ",end="")
    else:
      print(reg,",",end="")

  for stage in row[2]:
    print(stage," ",end="")
  print("\n")

