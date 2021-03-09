import math

x = [[1,2]]
for i in range(1, 1000):
  x.append([x[i-1][1],2*x[i-1][1]+x[i-1][0]])
for j in range(0, 1000):
  x[j][0] += x[j][1]
tot = 0
for element in x:
  if (math.floor(math.log10(element[0])) > math.floor(math.log10(element[1]))):
    tot += 1
print(tot)

