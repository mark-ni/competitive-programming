import time
t = time.time()

with open('revegetate.in','r') as fin:
  firstLine = fin.readline().strip().split(' ')
  N = int(firstLine[0])
  M = int(firstLine[1])

  cows = []
  for i in range(M):
    cow = fin.readline().strip().split(' ')
    cow[1] = int(cow[1])
    cow[2] = int(cow[2])
    cows.append(cow)

numSols = "1"
#find how many independent chains there are
pastures = ['' for i in range(N+1)]
pasturesStartUps = ['' for i in range(N+1)]
whosTogether = {}

def stripZero(num):
  return num[0:len(num)-1]

for cow in cows:
  #cow[1] unoccupied
  if pastures[cow[1]] == '':
    #cow[2] unoccupied
    if pastures[cow[2]] == '':
      pasturesStartUps[cow[1]] = cow[1]
      pasturesStartUps[cow[2]] = cow[1]
      whosTogether[cow[1]] = [cow[1]]
      numSols += '0'
      pastures[cow[1]] = True
      if cow[0] == 'S':
        pastures[cow[2]] = pastures[cow[1]]
      else:
        pastures[cow[2]] = not pastures[cow[1]]
    #cow[2] occupied
    else:
      pasturesStartUps[cow[1]] = pasturesStartUps[cow[2]]
      if cow[0] == 'S':
        pastures[cow[1]] = pastures[cow[2]]
      else:
        pastures[cow[1]] = not pastures[cow[2]]
  #cow[1] occupied
  else:
    #cow[2] unoccupied
    if pastures[cow[2]] == '':
      pasturesStartUps[cow[2]] = pasturesStartUps[cow[1]]
      if cow[0] == 'S':
        pastures[cow[2]] = pastures[cow[1]]
      else:
        pastures[cow[2]] = not pastures[cow[1]]
    #Both occupied
    else:
      if pasturesStartUps[cow[1]] not in whosTogether[pasturesStartUps[cow[2]]]:
        whosTogether[pasturesStartUps[cow[2]]].extend(whosTogether[pasturesStartUps[cow[1]]])
        whosTogether[pasturesStartUps[cow[1]]] = whosTogether[pasturesStartUps[cow[2]]]
        numSols = stripZero(numSols)
      else:
        if cow[0] == 'S':
          if pastures[cow[2]] != pastures[cow[1]]:
            numSols = '0'
            break
        elif cow[0] == 'D':
          if pastures[cow[2]] == pastures[cow[1]]:
            numSols = '0'
            break

if numSols != '0':
  for pasture in pastures:
    if pasture == '':
      numSols += '0'
  numSols = stripZero(numSols)

print(numSols)
with open('revegetate.out','w') as fout:
  fout.write(numSols)
print(time.time() - t)
