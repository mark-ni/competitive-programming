"""
ID: markni11
LANG: PYTHON3
TASK: sprime
"""
import math

fin = open('sprime.in', 'r')
fout = open('sprime.out', 'w')
input = fin.readline

odds = [1,3,7,9]

def isPrime(x):
    if x % 2 == 0:
        if x == 2:
            return True
        return False
    for i in range(3, int(math.sqrt(x)), 2):
        if x % i == 0:
            return False
    return True

def getPrimes(length):
  if (length == 1):
    return [2,3,5,7]
  else:
    s = [-1] * (4**length)
    prev = getPrimes(length - 1)
    currIndex = 0;
    for i in prev:
      for j in odds:
        if isPrime(i * 10 + j):
          s[currIndex] = i * 10 + j
          currIndex += 1
    return s[:currIndex]


n = int(input())
for i in getPrimes(n):
    fout.write(str(i) + "\n")
fout.close()
