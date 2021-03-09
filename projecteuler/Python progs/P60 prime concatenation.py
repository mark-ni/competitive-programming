
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

def satisfies1(p1, p2):
  return isPrime(int(str(p1) + str(p2))) and isPrime(int(str(p2) + str(p1)))

def satisfies2(p1, listp2):
  for p2 in listp2:
    if p1 == p2 or not satisfies1(p1, p2):
      return False
  return True

def generatePrimes(start, limit, rate=6):
  p = []
  for i in range(start, limit, rate):
    if isPrime(i):
      p.append(i)
  return p
#cases:
#add 5 cases at each step --> 5**4 = 625 cases per
#starts at 7
#starts at 11
def addList(li, e):
  l = li.copy()
  l.append(e)
  return l

def gList(primeList):
  l = len(primeList)
  triggered = False
  for a in range(l - 4):
    aurrList = [primeList[a]]
    #if satisfies2(primeList[a], currList):
    #  currList.append(primeList[a])
    for b in range(a+1, l - 3):
      burrList = aurrList.copy()
      if satisfies2(primeList[b], aurrList):
        burrList.append(primeList[b])
        for c in range(b+1, l - 2):
          CurrList = burrList.copy()
          if satisfies2(primeList[c], burrList):
            CurrList.append(primeList[c])
            for d in range(c + 1, l - 1):
              durrList = CurrList.copy()
              if satisfies2(primeList[d], CurrList):
                durrList.append(primeList[d])
                print(durrList)
                for e in range(d + 1, l):
                  if satisfies2(primeList[e], durrList):
                    print(durrList)
                    print(primeList[e])
                    print(sum(durrList) + primeList[e])
                    print("-----")

def generateList(startList, primeList, runningSums):
  if len(startList) == 4:
    runningSums.append(startList)
  else:
    count = 0
    cases = []
    for i in primeList:
      if satisfies2(i, startList):
        count += 1
        cases.append(i)
        if count == 6:
          break
    for case in cases:
      generateList(addList(startList,case),primeList,runningSums)
  return runningSums

x7 = generatePrimes(7, 10000)
x7.insert(0, 3)

print(gList(x7))

#98003