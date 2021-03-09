with open('mountains.in', 'r') as fin:
  count = int(fin.readline().strip())
  mountainList = []
  for i in range(count):
    line = fin.readline().strip().split(' ')
    x = int(line[0])
    y = int(line[1])
    b1 = x + y
    b2 = y - x
    fax = False
    for mountain in mountainList:
      if b1 <= mountain[0] and b2 <= mountain[1]:
        fax = True
        break
    if not fax:
      for mountain in mountainList:
        if b1 >= mountain[0] and b2 >= mountain[1]:
          mountainList.remove(mountain)
      mountainList.append([b1, b2])

with open('mountains.out', 'w') as fout:
  fout.write(str(len(mountainList)))
  fout.close
