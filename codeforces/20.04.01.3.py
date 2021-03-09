from sys import stdin
input=stdin.readline
t=int(input())
d=[0 for i in range(t)]
c=[0]*(t+1)
for i in range(t-1):
    u,v=map(int,input().split())
    c[u]+=1
    c[v]+=1
    d[i]=[u,v]
tgt=0
for i in range(1,t+1):
    if c[i] > 2:
        tgt=i
        break
if tgt==0:
    for i in range(t-1):
        print(i)
else:
    nums=set(range(3,t-1))
    count=0
    for i in range(t - 1):
        if tgt in d[i] and count < 3:
            print(count)
            count += 1
        else:
            print(nums.pop())

        
        


    
