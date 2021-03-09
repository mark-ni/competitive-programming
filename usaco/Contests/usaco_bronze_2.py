with open('sleepy.in', 'r') as fin:
  count = int(fin.readline().strip())
  order = []
  for num in fin.readline().strip('\n').split(' '):
    order.append(int(num))

i = count - 1
while i > 0:
  if (order[i] < order[i-1]):
    break
  i -= 1

with open('sleepy.out', 'w') as fout:
  fout.write(str(i))
  fout.close
