import time
t = time.time()

xmax = 1000
ymax = 1000

with open('paintbarn.in','r') as fin:
  maxXs = []
  maxYs = []
  firstLine = fin.readline().strip().split(' ')
  N = int(firstLine[0])
  K = int(firstLine[1])
  rects = []
  for i in range(N):
    rects.append(list(map(int,fin.readline().strip().split(' '))))
  coors = []
  for x in range(xmax):
    coors.append([0 for y in range(ymax)])

realCoors = []
for rect in range(0, N-K+1):
  for x in range(rects[rect][0], rects[rect][2]):
    for y in range(rects[rect][1], rects[rect][3]):
      coors[x][y] += 1
      realCoors.append([x,y])

def contains(coordinate, rectangle):
  if coordinate[0] >= rectangle[0]:
    if coordinate[0] < rectangle[2]:
      if coordinate[1] >= rectangle[1]:
        if coordinate[1] <rectangle[3]:
          return True
  return False

count = 0
for coor in realCoors:
  for rect in range(N-K+1, N):
    if contains(coor, rects[rect]):
      coors[coor[0]][coor[1]] += 1
    layers = coors[coor[0]][coor[1]]
    if layers > K:
      break
  if layers == K:
    count += 1

with open('paintbarn.out','w') as fout:
  fout.write(str(count))
print(time.time() - t)
