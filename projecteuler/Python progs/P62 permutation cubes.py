import math

#morphable
numDigits = 12
permutationCounts = 5
#variables
lowLimit = math.floor(10**((numDigits - 1)/3)) + 1
print(lowLimit)
upLimit = math.ceil(10**(numDigits/3))
print(upLimit)

def numToDigits(num):
  '''numToDigits(int) --> list'''
  digList = []
  while num > 0:
    digList.append(num % 10)
    num//=10
  return sorted(digList)

sols = [140283769536,536178930624,613258407936,913237656408,936302451687]
#for i in sols:
#  print(numToDigits(i))
#  print(i**(1/3))

cubeList = []
for i in range(lowLimit, upLimit):
  x = i**3
  cubeList.append(numToDigits(x))

argh = []
for h in cubeList:
  if cubeList.count(h) == permutationCounts:
    argh.append(h)
    print(h)

argh = min(argh)

for i in range(lowLimit, upLimit):
  if sorted(numToDigits(i**3)) == argh:
    print(i**3)
    break

