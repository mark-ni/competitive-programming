
def isTriangular(n):
  return math.sqrt(1 + 8 * n).is_integer()

def isSquare(n):
  return math.sqrt(4 * n) % 2 == 0

def isPentagonal(n):
  return math.sqrt(1 + 24 * n) % 6 == 5

def isHexagonal(n):
  return math.sqrt(1 + 8 * n) % 4 == 3

def isHeptagonal(n):
  return math.sqrt(9 + 40 * n) % 10 == 7

def isOctagonal(n):
  return math.sqrt(4 + 12 * n) % 6 == 4

tris = []
trisFirst = []
squares = []
squaresFirst =[]
pents = []
pentsFirst = []
hexs = []
hexsFirst = []
hepts = []
heptsFirst = []
octas = []
octasFirst = []

for i in range(1000, 10000):
  if isTriangular(i) and str(i)[2] != '0':
    tris.append([i//100, i % 100])
    trisFirst.append(i//100)
  if isSquare(i) and str(i)[2] != '0':
    squares.append([i//100, i % 100])
    squaresFirst.append(i//100)
  if isPentagonal(i) and str(i)[2] != '0':
    pents.append([i//100, i % 100])
    pentsFirst.append(i//100)
  if isHexagonal(i) and str(i)[2] != '0':
    hexs.append([i//100, i % 100])
    hexsFirst.append(i//100)
  if isHeptagonal(i) and str(i)[2] != '0':
    hepts.append([i//100, i % 100])
    heptsFirst.append(i//100)
  if isOctagonal(i) and str(i)[2] != '0':
    octas.append([i//100, i % 100])
    octasFirst.append(i//100)
squares.remove([10,24])
squares.remove([12,25])
squaresFirst.remove(10)
squaresFirst.remove(12)

def remove(li, e):
  l = []
  for i in range(len(li)):
    if not li[i] == e:
      l.append(li[i])
  return l

def getAns(currString, optionsAvailable):
  if len(optionsAvailable) == 0:
    if (currString[:2] == currString[len(currString) - 2:]):
      print("SUCCESS: " + currString)
    return
  
  lastTwo = int(currString[len(currString) - 2:])

  for b in optionsAvailable:
    if b == 4:
      if lastTwo in squaresFirst:
        getAns(currString + str(squares[squaresFirst.index(lastTwo)][1]),
        remove(optionsAvailable, b))
    elif b == 5:
      if lastTwo in pentsFirst:
        getAns(currString + str(pents[pentsFirst.index(lastTwo)][1]),
        remove(optionsAvailable, b))
    elif b == 6:
      if lastTwo in hexsFirst:
        getAns(currString + str(hexs[hexsFirst.index(lastTwo)][1]),
        remove(optionsAvailable, b))
    elif b == 7:
      if lastTwo in heptsFirst:
        getAns(currString + str(hepts[heptsFirst.index(lastTwo)][1]),
        remove(optionsAvailable, b))
    elif b == 8:
      if lastTwo in octasFirst:
        getAns(currString + str(octas[octasFirst.index(lastTwo)][1]),
        remove(optionsAvailable, b))

for i in tris:
  getAns(str(i[0]) + str(i[1]), [4,5,6,7,8])