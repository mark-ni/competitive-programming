from collections import deque
from sys import stdin,stdout
input=stdin.readline

def getAns(li):
    odds = deque()
    evens = deque()
    for i in li:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    evens.append(10)
    odds.append(10)
    ans = [0]*len(li)
    i = 0
    while i < len(li):
        if evens[0] < odds[0]:
            ans[i] = evens.popleft()
        else:
            ans[i] = odds.popleft()
        i += 1
    for i in ans:
        stdout.write(str(i))

for _ in range(int(input())):
    getAns(list(map(int,input().rstrip())))
    stdout.write('\n')
