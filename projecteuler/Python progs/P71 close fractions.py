
import math
import time

t = time.time()

primeList = [2]
currentclosest = 1
currentclosestnum = 0
for i in range(1, 1000000):
  if i % 7 != 0:
    diff = 3/7 - math.floor(3*i/7)/i 
    if diff < currentclosest:
      currentclosest = diff
      currentclosestnum = i 
print(math.floor(3 * currentclosestnum / 7))



print(time.time() - t)