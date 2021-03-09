import math

tot = 0
for numDigits in range(2, 100):
  lowLimit = math.floor(10**((numDigits - 1)/numDigits)) + 1
  tot += 10 - lowLimit
print(tot + 9)
