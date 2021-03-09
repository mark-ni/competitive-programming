from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for _ in range(t):
        a,b,c,d=map(int,input().split())
        x,y,x1,y1,x2,y2=map(int,input().split())
        netr=b-a
        netu=d-c
        if x1 == x2 and (a > 0 or b > 0):
            print("No")
            continue
        if y1 == y2 and (c > 0 or d > 0):
            print("No")
            continue
        if netr + x < x1 or netr + x > x2:
            print("No")
            continue
        if netu + y < y1 or netu + y > y2:
            print("No")
            continue
        print("Yes")
        
def B():
    t=int(input())
    for _ in range(t):
        m=int(input())
        a=list(map(int,input().split()))
        c=[0]*m
        p=[2,3,5,7,11,13,17,19,23,29,31]
        used=[False]*11
        for i in range(m):
            j = 0
            while a[i] % p[j] != 0:
                j += 1
            used[j] = True
            c[i] = j
        used[0] = int(used[0])
        for i in range(1, 11):
            used[i] = int(used[i]) + used[i - 1]
        for i in range(m):
            c[i] = used[c[i]]
        print(max(used))
        print(*c)

def C():
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        s=[ord(x) - 97 for x in input().rstrip()]
        l=[[0 for i in range(26)] for j in range(k)]
        for i in range(n):
            l[i % k][s[i]] += 1
        for i in range(k//2):
            for j in range(26):
                l[i][j] += l[k-i-1][j]
        for i in range((k + 1)//2):
            n -= max(l[i])
        print(n)

def D():
    k=int(input())
    if k == 0:
        print("1 1\n1")
    else:
        t=1
        while t <= 2*k:
            t*=2
        print('3 2')
        print(str(t-1) + ' ' + str(t//2))
        print(str(k) + ' ' + str(t - 1))
        print('0 ' + str(t//2 - 1))
D()
#a&d=q
#b > c, b & f = 0, c & f = k#

#63  32
#k   63
#    31
#q=
