with open('perimeter.in', 'r') as fin:
  count = int(fin.readline().strip())
  li = []
  for i in range(count):
    li.append(list(fin.readline().strip()))

  coordinates = []
  for q in range(count):
    for r in range(count):
      if li[q][r] == "#":
        coordinates.append([q,r])

def findMyPeople(location):
  perimeter[0] += 4 
  x = location[0]
  y = location[1]
  alreadyVisited.append(location)
  if x > 0:
    a = [x-1,y]
    if li[a[0]][a[1]] == '#':
      perimeter[0] -= 1
      if a not in alreadyVisited:
        findMyPeople(a)
  if x < count - 1:
    a = [x+1,y]
    if li[a[0]][a[1]] == '#':
      perimeter[0] -= 1
      if a not in alreadyVisited:
        findMyPeople(a)
  if y > 0:
    a = [x,y-1]
    if li[a[0]][a[1]] == '#':
      perimeter[0] -= 1
      if a not in alreadyVisited:
        findMyPeople(a)
  if y < count - 1:
    a = [x,y+1]
    if li[a[0]][a[1]] == '#':
      perimeter[0] -= 1
      if a not in alreadyVisited:
        findMyPeople(a)
  return

checked = []
highests = [[0,0]]

for pair in coordinates:
  alreadyVisited = []
  perimeter = [0]
  findMyPeople(pair)
  if len(alreadyVisited) >= highests[0][0]:
    if len(alreadyVisited) == highests[0][0]:
      highests.extend([len(alreadyVisited),perimeter[0]])
    else:
      highests = [[len(alreadyVisited), perimeter[0]]]
  for element in alreadyVisited:
    coordinates.remove(element)

perimeters = []
for e in highests:
  perimeters.append(e[1])
for f in highests:
  if f[1] == min(perimeters):
    perimeter = f[1]
area = highests[0][0]

with open('perimeter.out', 'w') as fout:
  fout.write(str(area) + " " + str(perimeter))
  fout.close
