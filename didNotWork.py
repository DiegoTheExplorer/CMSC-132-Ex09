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

  for i in range(4,0,-1):
    if((i == 4) & (pipeline[i][1] != None)):
      finished.append(copy.deepcopy(pipeline[i][1]))
      pipeline[i][1] = None
    
    if((pipeline[i-1][1] != None) & (i != 1)):
      pipeline[i][1] = copy.deepcopy(pipeline[i-1][1])
      pipeline[i][1][2].append(pipeline[i][0])
      pipeline[i-1][1] = None

    elif((pipeline[i-1][1] != None) & i == 1):
      db = pipeline[i-1][1][1]
      curr = set(pipeline[i-1][1][1])
      hasRegInUse = False
      for j in range(1,4):
        if(pipeline[j][1] != None):
          cmp = set(pipeline[j][1][1])
          if(len(curr & cmp) != 0):
            hasRegInUse = True
            break
      if(hasRegInUse):
        pipeline[i-1][1][2].append('S')
      else:
        pipeline[i][1] = copy.deepcopy(pipeline[i-1][1])
        pipeline[i][1][2].append(pipeline[i][0])
        pipeline[i-1][1] = None

  if((len(ins) != 0) & (pipeline[0][1] == None)):
    pipeline[0][1] = ins.pop(0)
    pipeline[0][1][2].append(pipeline[0][0])

  for stage in pipeline:
    print(stage)
  print("******************************************")

for inst in finished:
  print(inst)

# while(not (ins[len(ins) - 1][4])):
#   if(time == 0):
#     for i in range(0,(len(ins))):
#       stall = False
#       if(i == 0):
#         ins[i][3] += 1
#       ins[i][2].append(pipeline[ins[i][3]])
  
#   else:
#     for i in range(0,(len(ins))):
#       if(i == 0):
#         ins[i][3] += 1
#         ins[i][2].append(pipeline[ins[i][3]])
#       elif(0 < i):
#         if(not ((ins[i - 1][3] == 0) or (ins[i - 1][3] == 1))):
#           ins[i][3] += 1
#           ins[i][2].append(pipeline[ins[i][3]])
#         if(ins[i][3]):

#       if(ins[i][3] > 5):
#         ins[i][4] = True