import math
import time

t = time.time()

def takeAway(li, e):
  '''completely unnecessary function but whatever'''
  l = []
  for x in li:
    if x != e:
      l.append(x)
  return l
 
listOfNums = []
 
aheSet = [9,8,7, 6, 5, 4, 3, 2, 1]
for a in aheSet:
  bheSet = takeAway(aheSet, a)
  for b in bheSet:
    cheSet = takeAway(bheSet, b)
    for c in cheSet:
      dheSet = takeAway(cheSet, c)
      for d in dheSet:
        eheSet = takeAway(dheSet, d)
        if 10 + a == c + d:
          for e in eheSet:
            fheSet = takeAway(eheSet, e)
            for f in fheSet:
              gheSet = takeAway(fheSet, f)
              if b + c == e + f:
                for g in gheSet:
                  hheSet = takeAway(gheSet, g)
                  for h in hheSet:
                    if g + h == e + d:
                      i = takeAway(hheSet, h)[0]
                      if a + i == g + f:
                        listOfNums.append([[c,b,d],[e,d,f],[g,f,h],[i,h,a],[10,a,b]])
stringList = []
for x in listOfNums:
  smallestNode = 0
  firstOuters = []
  string = ""
  for y in x:
    firstOuters.append(y[0])
  smallestNodeIndex = firstOuters.index(min(firstOuters))
  mod = len(x)
  for z in range(smallestNodeIndex, smallestNodeIndex + mod, 1):
    for aa in x[z % mod]:
      string += str(aa)
  stringList.append(int(string))
print(max(stringList))

#0.0135 seconds

print(time.time() - t)
