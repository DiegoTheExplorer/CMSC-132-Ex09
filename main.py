#Diego Miguel M. Villamil
#CMSC 132 AB2L
#Exercise 9

import copy


#Read instructions from given filename
def readIns(filename):
  instructions = []

  fp = open(filename, "r")

  for line in fp:
    temp = line.strip()
    temp = temp.split(" ")
    temp[1] = temp[1].split(",")
    temp.append([])
    instructions.append(temp)
    print(temp)
    
  return instructions

#Start of main
ins = readIns("input.in")
pipeline = [["F",None],["D",None],["E",None],["M",None],["W",None]]
finished = []
numIns = len(ins)

while(len(finished) != numIns):
  if(len(ins) != 0):
    pipeline[0][1] = ins.pop(0)
  temp = None
  for i in range(4,0,-1):
    if((i == 4) & (pipeline[i][1] != None)):
      finished.append(copy.deepcopy(pipeline[i][1]))
      pipeline[i][1] = None
    
    pipeline[i][1] = copy.deepcopy(pipeline[i-1][1])
    pipeline[i-1][1] = None
  for stage in pipeline:
    print(stage)
  print("******************************************")

for inst in finished:
  print(inst)