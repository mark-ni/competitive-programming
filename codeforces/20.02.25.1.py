from collections import deque
def ORDd(x):
    if ord(x) >= 97:
        return ord(x) - 71
    return ord(x) - 65

n=int(input())
s=[ORDd(x) for x in input().rstrip()]
l=[0]*n
ogSet = set()
lastInd = 0
for i in range(n):
    if s[i] not in ogSet:
        ogSet.add(s[i])
        lastInd = i
for i in range(n):
    newSet = ogSet.copy()
    j = 0
    while len(newSet) > 0:
        if s[j] in newSet:
            newSet.remove(s[j])
        j += 1
    


length = input()        
string = input()
dictionary = {}
lengthOfString = len(set(string))
i,j = 0,0
l = length
while i < length:
    currMon = string[i]
    dictionary[currMon] = dictionary.get(currMon, 0) + 1
    if l == dictionary[currMon]:
        lengthOfString -= 1
    while j <= i and dictionary[string[j]] > 1:
        

