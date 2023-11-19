#Diego Miguel M. Villamil
#CMSC 132 AB2L
#Exercise 9

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
    


#Start of main
readIns("input.in")
pipeline = [["F",None],["D",None],["E",None],["M",None],["W",None]]