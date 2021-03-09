from sys import stdin
from collections import deque
input=stdin.readline
n=int(input())
letters=[deque() for i in range(26)]
nums=[deque() for i in range(n)]
lettersVisited=[False for i in range(26)]
numsVisited=[False for i in range(n)]
for i in range(n):
    for j in [ord(x)-ord('a') for x in input().rstrip()]:
        nums[i].appendleft(j)
        letters[j].appendleft(i)
def dfs1(i):
    lettersVisited[i] = True
    for to in letters[i]:
        if not numsVisited[to]:
            dfs2(to)

def dfs2(i):
    numsVisited[i] = True
    for to in nums[i]:
        if not lettersVisited[to]:
            dfs1(to)
tot=0
for i in range(26):
    if len(letters[i]) > 0 and not lettersVisited[i]:
        dfs1(i)
        tot+=1
print(tot)

        
    

    
