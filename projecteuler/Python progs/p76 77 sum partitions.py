import math
import time
t = time.time()
 
def generatePrimeFactors(num):
  q = []
  for i in range(1, math.floor(num/2) + 1):
    if num % i == 0:
      q.append([i, num//i])
  return q

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
#6 -- [1,1,0]
#7 -- [0,0,1]
#8 -- [1,1,1,0]
#17 -- [0,3, 12 largest 5, 10 largest 7 = 5, 6 largest 11
#23 -- [0, 20 largest index 1, 18 largest index 2, 16 largest index 3,12 largest index 11, 10 largest index 3]
#25 -- 20, largest 5

primeList = [2]
for i in range(3, 1500, 2):
  if isPrime(i):
    primeList.append(i)

li = [[],[],[],[0],[1,0],[0,1]]
for i in range(6,150):
  diffList = []
  diffList.append(int(i % 2 == 0))
  currentPrimeIndex = 1
  while primeList[currentPrimeIndex] < i:
    tot = 0

    highPrime = primeList[currentPrimeIndex]
    diff = i - highPrime
    if highPrime >= diff:
      newHighPrime = diff
      if isPrime(diff):
        tot += 1
  
    else:
      newHighPrime = highPrime
    diffList.append(sum(li[diff][0:currentPrimeIndex+1])+tot)
    currentPrimeIndex += 1

  li.append(diffList)
  if sum(diffList) > 5000:
    print(i)
    break
print(t - time.time())