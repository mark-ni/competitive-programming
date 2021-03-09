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
  factSet.add(n)
  return factSet

def phi(n):
  for h in primeFactors(n):
    n = n//h * (h -1)
  return n

def isSetOf(n1, n2):
  if len(str(n1)) != len(str(n2)):
    return False 

  n1set = []
  for i in range(math.floor(math.log10(n1))+1):
    n1set.append(n1 % 10)
    n1//=10
  n2set = []
  for i in range(math.floor(math.log10(n2))+1):
    n2set.append(n2 % 10)
    n2//=10
  if sorted(n1set) == sorted(n2set):
    return True
  return False

primeList = [2]
for i in range(3, 10000, 2):
  if isPrime(i):
    primeList.append(i)

minimum = 2
minimumcombo = 0
for prime1 in primeList:
  for prime2 in primeList:
    product = prime1 * prime2
    if (product < 10**7):
      if isSetOf(product,(prime1 - 1) * (prime2 - 1)):
        dividend = (prime1 - 1) * (prime2 - 1)
        if (product/dividend) < minimum:
          minimum = product/dividend
          minimumcombo = product
          print(str(product) + ": " + str(phi(product)))
