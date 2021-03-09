import math
import time
thetime = time.time()


def isPrime(num):
  '''isPrime(int) --> bool'''
  if (num < 3):
    if num < 0:
      num *= -1
    elif num == 1:
      return False
    elif num == 2:
      return True
  if (num % 2 == 0):
    return False
  for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
    if (num % i == 0):
      return False
  return True

def getEmptyFacts(num):
  facts = {}
  for i in range(2, num + 1):
    if num % i == 0:
      print(3)

primeList = []
for asdfasdf in range(2, 100):
  #if isPrime(asdfasdf):
  primeList.append(asdfasdf)

#x^2 - 1/D = y^2
#x**2 = Dk + 1 --> Dk * (Dk + 2) = 
#(x+1)(x-1)/D = y**2

#odds --> 7, 23, 31, 47, 61, 71, 79, 103, 109, 127, 151, 157, 

theList = []
for D in primeList:
  seq = 0
  x = 2
  k = 1
  while True:
    if (seq % 2 == 0):
#      if math.sqrt((k * D - 2) * k).is_integer():
#        theList.append(k * D - 1)
      if math.sqrt((x-1)*(x+1)/D).is_integer():
        theList.append(x)
        print(str(D) + ": " + str(x))
        break
      x += 1
    else:
      #if math.sqrt((k * D + 2) * k).is_integer():
      #  theList.append(k * D + 1)

      if math.sqrt((x+1)*(x-1)/D).is_integer():
        theList.append(x)
        print(str(D) + ": " + str(x) + ", odd!")
        break
      k += 1
      x += 1
    seq += 1


print(time.time() - thetime)
