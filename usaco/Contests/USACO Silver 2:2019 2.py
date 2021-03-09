import time
t = time.time()

xmax = 1000
ymax = 1000

with open('paintbarn.in','r') as fin:
  firstLine = fin.readline().strip().split(' ')
  N = int(firstLine[0])
  K = int(firstLine[1])
  rects = []
  for i in range(N):
    rects.append(list(map(int, fin.readline().strip().split(' '))))
  coors = []
  for x in range(xmax):
    coors.append([0 for y in range(ymax)])

for rect in rects:
  for x in range(rect[0], rect[2]):
    for y in range(rect[1], rect[3]):
      coors[x][y] += 1

count = 0
for x in range(xmax):
  for y in range(ymax):
    if coors[x][y] == K:
      count += 1

print(count)

with open('paintbarn.out','w') as fout:
  fout.write(str(count))
print(time.time() - t)
