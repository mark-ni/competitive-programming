fin = open('shell.in','r')

counts = fin.readline()
theList = []
for count in range(int(counts)):
  theList.append(fin.readline().strip('\n').split(' '))
  theList[count] = [int(theList[count][n]) for n in range(3)]

startingList = [0, True, False, False]

def transform(start):
  score = 0
  for count in range(int(counts)):
    currentList = theList[count]
    placeHolder = start[currentList[0]]
    start[currentList[0]] = start[currentList[1]]
    start[currentList[1]] = placeHolder
    score += start[currentList[2]]
  
  return score

scores = []

for li in [[0, True, False, False,],[0, False, True, False],[0, False, False, True]]:
  scores.append(transform(li))

with open('shell.out', 'w') as fout:
  fout.write(str(max(scores)))
  fout.close
