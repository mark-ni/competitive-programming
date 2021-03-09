#from sys import stdin,stdout
#input=stdin.readline
def a():
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        if a % b == 0: print(0)
        else: print(str(b-(a%b)))

def b():
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        bpos1 = 0
        bpos2 = 0
        for i in range(2,n + 1):
            asdf = i * (i - 1) // 2
            if asdf >= k:
                bpos1 = i
                bpos2 = bpos1 - (asdf - k) - 1
                break
        string = ['a'] * n
        string[n - bpos1] = 'b'
        string[n - bpos2] = 'b'
        print(''.join(string))

def c():
    t=int(input())
    for _ in range(t):
        n=int(input())
        x=[int(i) for i in input().rstrip()]
        a = [0]*n
        b = [0]*n
        ind = 0
        for i in x:
            if i == 0:
                a[ind] = 0
                b[ind] = 0
            elif i == 1:
                a[ind] = 1
                b[ind] = 0
                break
            else:
                a[ind] = 1
                b[ind] = 1
            ind += 1
        for i in range(ind + 1, n):
            b[i] = x[i]
        for i in a:
            stdout.write(str(i))
        stdout.write('\n')
        for i in b:
            stdout.write(str(i))
        stdout.write('\n')

def d():
    q=int(input())
    for _ in range(q):
        n=int(input())
        t=list(map(int,input().split()))
        colors = [1]*n
        same=True
        for i in range(1,n):
            if t[i] != t[i - 1]:
                same=False
                break
        if same:
            print(1)
            print(*colors)
        else:
            for i in range(1,n):
                colors[i] = colors[i - 1] % 2 + 1
            if n % 2 == 0:
                print(2)
                print(*colors)
            else:
                ind=-1
                if t[0] == t[n-1]: ind = n
                for i in range(1, n):
                    if t[i] == t[i - 1]:
                        ind = i
                        break
                if ind >= 0:
                    for i in range(ind, n):
                        colors[i] = colors[i] % 2 + 1
                    print(2)
                    print(*colors)
                else:
                    colors[n - 1] = 3
                    print(3)
                    print(*colors)

import io, os
input=io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def e():
    n,m=map(int,input().split())
    parents=[-1]*(n+1)
    parents[1]=0
    for i in range(n - 1):
        u,v=map(int,input().split())
        if u > v: v,u=u,v
        parents[v] = u
    for _ in range(m):
        v=[parents[int(i)] for i in input().split()]
        v[0] = 0
        v=sorted(set(v))
        length=len(v)
        i = length - 1
        flag=False
        currNode = v[length - 1]
        while i >= 0:
            if currNode <= v[i]:
                if currNode == v[i]:
                    i -= 1
                else:
                    flag=True
                    break
            currNode = parents[currNode]
        if flag: print("NO")
        else: print("YES")
e()
            
            
        
        
        
        
                
            
        
        
