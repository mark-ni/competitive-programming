
import math
import time

t = time.time()
lim = 1000000

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

def primeFactors(n):
  i = 0
  factSet = set([])
  while primeList[i] < n:
    factor = primeList[i]
    while n % factor == 0:
      n //= factor
      factSet.add(factor)
    i += 1
    if isPrime(n):
      factSet.add(n)
      return factSet
  if n != 1:
    factSet.add(n)
  return factSet

def phi(n):
  for h in primeFactors(n):
    n = n//h * (h -1)
  return n

primeList = [] #primeList = [2]
compList = []
for i in range(2, 1000001):#): for i in range(2, 1000000):
  if isPrime(i):
    primeList.append(i)
  else:
    compList.append(i)

print("done with easy part")
t = time.time()
tot = 0
for num in compList:
  tot += phi(num)
tot += 37550323525

print(tot)
#302143220713
#subtract 1

print(time.time() - t)