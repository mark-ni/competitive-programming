with open('guess.in', 'r') as fin:
  count = int(fin.readline().strip())
  animalList = []
  for i in range(count):
    line = fin.readline().strip().split(' ')
    animalList.append(set(line[2:]))

maxLength = 0
for li1 in animalList:
  if len(li1) > maxLength:
    for li2 in animalList:
      if (li1 != li2):
        if len(li2) > maxLength:
          length = len(li2.intersection(li1))
          if length > maxLength:
            maxLength = length

with open('guess.out', 'w') as fout:
  fout.write(str(maxLength + 1))
  fout.close
