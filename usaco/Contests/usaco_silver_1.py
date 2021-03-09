with open('planting.in', 'r') as fin:
  count = int(fin.readline().strip())
  pointList = [0 for n in range(count+1)]
  for i in range(count - 1):
    line = fin.readline().strip().split(' ')
    pointList[int(line[0])] += 1
    pointList[int(line[1])] += 1  

with open('planting.out', 'w') as fout:
  fout.write(str(max(pointList) + 1))
  fout.close
