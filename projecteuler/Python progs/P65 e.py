li = [2]
for i in range(1, 40):
  li.extend([1, 2 * i, 1])
print(li)

def expand(kIndex, stopIndex):
  if kIndex == stopIndex - 1:
    print([li[kIndex]*li[kIndex + 1] + 1, li[kIndex+1]])
    return [li[kIndex]*li[kIndex + 1] + 1, li[kIndex+1]]
  else:
    rightSide = expand(kIndex + 1, stopIndex)
    print([li[kIndex] * rightSide[0] + rightSide[1],rightSide[0]])
    return [li[kIndex] * rightSide[0] + rightSide[1],rightSide[0]]

#2 --> 3rd term

x = expand(0, 99)[0]
tot = 0
for i in str(x):
  tot += int(i)
print(tot)
