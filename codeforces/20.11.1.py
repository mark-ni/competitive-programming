from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for __ in range(t):
        l,r=map(int,input().split())
        if 2 * l > r:
            print("YES")
        else:
            print("NO")

def B():
    t=int(input())
    for __ in range(t):
        n=int(input())
        s=[bool(int(x)) for x in input().rstrip()]
        currT=0
        currF=0
        Ts=[]
        Fs=[]
        for i in s:
            if i:
                if currF > 1: Fs.append(currF-1)
                currF=0
                currT += 1
            else:
                if currT > 1: Ts.append(currT-1)
                currT=0
                currF += 1
        if currT > 1: Ts.append(currT - 1)
        elif currF > 1: Fs.append(currF - 1)
        print(max(sum(Ts),sum(Fs)))
        

def C():
    from collections import deque
    
    t=int(input())
    for __ in range(t):
        n=int(input())
        a=sorted(list(map(int,input().split())))
        busy=[False]*302
        l=deque()
        for i in range(n):
            a[i] -= 1
            if not busy[a[i]]:
                busy[a[i]]=True
            else:
                l.append(a[i])
        tot=0
        while len(l) > 0:
            x=l.popleft()
            i=x-1
            while i >= 0 and busy[i]:
                i -= 1
            j=x+1
            while j < len(busy) and busy[j]:
                j += 1
            #use left side
            if j == len(busy):
                tot += x - i
                busy[i] = True
            elif i < 0:
                tot += j - x
                busy[j] = True
            elif j - x >= x - i:
                tot += x - i
                busy[i] = True
            else:
                tot += j - x
                busy[j] = True
        print(tot)

def D():
    t=int(input())
    for __ in range(t):
        _=0

C()


a   b   c         d
could be b - a + d - c or c - b + d - a
