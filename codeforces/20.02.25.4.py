from collections import deque
n=int(input())
a=list(map(int,input().split()))
maxDiversity = 0
frontd = deque()
backd = deque()
frontp = {}
backp = {}
for i in a:
    frontp[i]=frontp.get(i,0)+1
    frontd.append(i)
    if frontp[i] >= 2:
        frontd.pop()
        break
for i in range(n - 1, -1, -1):
    curr=a[i]
    backp[curr]=backp.get(curr,0)+1
    backd.append(curr)
    if backp[curr] >= 2:
        backd.pop()
        break
best=[0]*len(frontd)
s=set()
stemp=set()
for j in backd:
    if j in stemp:
        break
    stemp.add(j)
best=[0]*len(frontd) + [len(stemp)]
for i in range(len(frontd)):
    s.add(frontd[i])
    stemp = set()
    for j in backd:
        if j in s or j in stemp:
            break
        stemp.add(j)
    best[i] = len(stemp) + len(s)
print(n - max(best))
    
    
