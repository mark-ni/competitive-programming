import time
t = time.time()

li = [[],[0],[0,1]]
for i in range(3,200):
  diffList = [0]

  for high in range(1, i):
    tot = 0
    diff = i - high
    if high >= diff:
      newHigh = diff
      tot += 1
    else:
      newHigh = high
    diffList.append(sum(li[diff][1:newHigh+1])+tot)

  li.append(diffList)
  print(i,sum(diffList)+1)

print(t - time.time())