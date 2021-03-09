from sys import stdin
input=stdin.readline
def A():
    for i in range(int(input())):print((int(input())-1)//2)

def B():
    for _ in range(int(input())):
        n,a,b=map(int,input().split())
        s='abcdefghijklmnopqrstuvwxyz'[0:b]*(n//b+1)
        print(s[0:n])
    return
def C():
    for _ in range(int(input())):
        n=int(input())
        d=[0]*(n+1)
        a=list(map(int,input().split()))
        for i in a:
            d[i]+=1
        one=max(d)-1
        two=len(set(a))
        if one < two:
            two -= 1
            one += 1
        print(min(one,two))
        
    return
def D():
    for _ in range(int(input())):
        l=[[0 for i in range(9)] for j in range(9)]
        for i in range(9):
            s=input().rstrip()
            for j in range(9):
                l[i][j]=s[j]
        p=[(0,0),(1,3),(2,6),(3,1),(4,4),(5,7),(6,2),(7,5),(8,8)]
        for i,j in p:
            l[i][j]=str(int(l[i][j])%9 + 1)
        for row in l:
            print(''.join(row))
    return
D()
