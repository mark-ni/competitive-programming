from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        a=sorted(list(map(int,input().split())))
        tot=0
        for i in range(1, n):
            tot += (k-a[i])//a[0]
        print(tot)

def B():
    from collections import defaultdict
    t=int(input())
    for _ in range(t):
        n,T=map(int,input().split())
        a=list(map(int,input().split()))
        d=defaultdict()
        colors=[0]*n
        for i in range(n):
            colors[i] = d.get(a[i],0)
            d[T-a[i]] = (1 + colors[i]) % 2
        print(*colors)

def C():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        nums=[[] for i in range(n+1)]
        for i in range(n):
            nums[a[i]].append(i)
        s=[300001]*(n+1)
        for i in range(len(nums)):
            if len(nums[i]) > 0:
                maxdist=max(nums[i][0]+1,n-nums[i][-1])
                for j in range(1,len(nums[i])):
                    maxdist=max(maxdist,nums[i][j]-nums[i][j-1])
                s[maxdist] = min(s[maxdist],i)
        ans=[s[1]]*n
        for i in range(1,n):
            ans[i] = min(ans[i-1],s[i+1])
        for i in range(n):
            if ans[i]==300001: ans[i] = -1
        print(*ans)

def D():
    from math import ceil
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        avg=sum(a)//n
        if n * avg != sum(a):
            print(-1)
            continue
        ans=[]
        first=a[0]
        for i in range(1,n):
            if a[i] >= i + 1:
                ans.append([i+1,1,a[i]//(i+1)])
                first+=a[i]//(i+1)
                a[i] %= (i+1)
        g=[]
        for i in range(1,n):
            if a[i] > avg:
                k=(-1 * (a[i] - avg)) % (i + 1)
                g.append([k,1,i+1])
                ans.append([1,i+1,k])
                a[i] += k
                ans.append([i+1,1,(a[i]-avg)//(i+1)])
        for i in range(1,n):
            if a[i] < avg:
                ans.append([1,i+1,avg+i+1-a[i]])
                ans.append([i+1,1,1])
        print(len(ans))
        for i in ans:
            print(*i)
D()
                
                
            
