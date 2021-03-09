
import math
import time

t = time.time()

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

def sharesFactors(a, b):
  if isPrime(b):
    return False
  i = 0
  while primeList[i] <= b:
    factor = primeList[i]
    if b % factor == 0 and a % factor == 0:
      return True
    i += 1
  return False

#primeList = [2] #primeList = [2]
#for i in range(3, 6000):#): for i in range(2, 1000000):
#  if isPrime(i):
#    primeList.append(i)
#
#tot = 0

#for a in range(2001, 4001):
#  for b in range(math.floor(a/3) + 1, math.ceil(a/2)):
#    if not sharesFactors(a,b):
#      tot += 1
#print(tot)

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

primeList = [2,3] #primeList = [2]
compList = []
for i in range(4, 12001):#): for i in range(2, 1000000):
  if isPrime(i):
    primeList.append(i)
  else:
    compList.append(i)

print("done with easy part")
t = time.time()
tot = 0
for num in primeList[2:]:
  tot += int(math.floor(num/2) + 1 - math.ceil(num/3))
print(tot)
#for a in compList[0:50]:
#  for b in range(math.floor(a/3) + 1, math.ceil(a/2)):
#    if not sharesFactors(a,b):
#      tot += 1
#      print(str(b) + "/" + str(a))
print(tot)
primeSum = 1339075

print(5956298 + 1339074)
#4 to 2000 - 202766, 26 seconds
#2001 to 4000 - 607831, 3 minutes
#4001 to 6000: 1017495, 38s
#6001 to 8000: 1423753, 62s
#8001 to 10000: 1829192, 83.9s
#10001 to 12000: 2235178, 132s

print(time.time() - t)