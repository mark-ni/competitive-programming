from sys import stdin
input=stdin.readline

def printTable(u):
    for _ in u:
        print(*_)

def getAns(s,t):
    l=len(s)
    l2=len(t)
    rows,cols=(l,26)
    u = [[-1 for i in range(cols)] for j in range(rows)]
    currLetterIndices = [-1]*26
    for j in range(26):
        if j in s:
            ind = s.index(j)
            currLetterIndices[j] = 0
            for i in range(l):
                u[i][j] = ind
    for i in range(l):
        currLetter = s[i]
        for k in range(currLetterIndices[currLetter], i):
            u[k][currLetter] = i
        currLetterIndices[currLetter] = i
        #for j in range(26):
        #    u[i][j] = currLetterIndices[j]
    #printTable(u)
    currIndex = -1
    cycles = 1
    for letter in t:
        newIndex = u[currIndex][letter]
        if newIndex <= currIndex:
            cycles += 1
            if newIndex == -1:
                return -1
        currIndex = newIndex
    return cycles
    
    #u = s*((26*l2)//l + 1)
    #currIndex = 0
    #for i in range(len(u)):
    #    if u[i] == t[currIndex]:
    #        currIndex += 1
    #        if currIndex == l2:
    #            return i//l + 1
    #return -1

for _ in range(int(input())):
    s=[ord(x)-97 for x in input().rstrip()]
    t=[ord(x)-97 for x in input().rstrip()]
    print(getAns(s,t))

#make s have length 26*t,

