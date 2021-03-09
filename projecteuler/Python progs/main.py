import math
import time
t = time.time()

x = [[1,2]]
for i in range(1, 10):
  x.append([x[i-1][1],2*x[i-1][1]+x[i-1][0]])
for j in range(0, 10):
  x[j][0] += x[j][1]
tot = 0
print(x)

print(tot)


print(time.time()-t)