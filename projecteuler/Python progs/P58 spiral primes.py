
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

def getAnswer():
  lastUL = 1
  lastUR = 1
  lastDL = 1
  lastDR = 1
  runningPrimes = 0
  runningNums = 1
  rL = 1

  while True:
    lastUL = lastUL + 4 * rL + 2
    lastUR = lastUR + 4 * rL + 4
    lastDL = lastDL + 4 * rL + 0
    lastDR = lastDR + 4 * rL - 2

    rL += 2

    for num in [lastUL, lastUR, lastDL, lastDR]:
      if (isPrime(num)):
        runningPrimes += 1
    runningNums += 4

    if runningPrimes/runningNums <= 0.10:
      print(rL)
      return

getAnswer()

print(time.time() - thetime)
