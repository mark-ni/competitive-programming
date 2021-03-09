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

def reverse(i): 
  '''reverse(int i) --> int
  for example, 334 --> 433'''
  return int(str(i)[::-1])

def sumOfDigits(n):
  '''sumOfDigits(int n) --> int'''
  sod = 0
  for i in range(math.floor(math.log10(n))+1):
    sod += n % 10
    n //= 10
  return sod

#------More Obscure----------------
def isLychrel(num):
  '''isLychrel(int num) --> int
  if, after 50 trials, a number added to its reverse
  never produces a palindrome, it is said to be lychrel'''
  k = 0
  x = reverse(num)
  while (k < 50):
    num += x
    x = reverse(num)
    if num == x:
      return False
    k += 1
  return True