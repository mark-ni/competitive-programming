from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for _ in range(t):
        n=int(input())
        print(*[i for i in range(4*n-2,2*n-2,-2)])

def B():
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        m=list(map(int,input().rstrip()))
        prev=-1
        ones = 0
        zeros = 0
        currCost = 0
        for i in range(len(m)):
            if m[i] != prev and prev == 0 and ones > 0:
                currCost += min(b, zeros * a)
                zeros = 0
                ones = 0
            if m[i] == 1:
                ones += 1
            else:
                zeros += 1
            prev = m[i]
        print(currCost)
            
            
B()
