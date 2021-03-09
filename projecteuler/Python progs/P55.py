import math

def isLychrel(num):
  k = 0
  x = reverse(num)
  while (k < 50):
    num += x
    x = reverse(num)
    if num == x:
      return True
    k += 1
  return False

def sumOfDigits(n):
  sod = 0
  for i in range(math.floor(math.log10(n))+1):
    sod += n % 10
    n //= 10
  return sod


j = 0
for i in range(1,10000):
  if not isLychrel(i):
    j += 1
print(j)
