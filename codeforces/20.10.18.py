from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        print(a^b)
    
def B():
    from collections import deque
    t=int(input())
    for _ in range(t):
        n=int(input())
        square=[0 for i in range(n)]
        for i in range(n):
            square[i] = list(input().rstrip())
        a,b,c,d=square[0][1],square[1][0],square[n-2][n-1],square[n-1][n-2]
        ans=[]
        if a == '0' and b == '0':
            if c == '0': ans.append([n-2,n-1])
            if d == '0': ans.append([n-1,n-2])
        elif a == '1' and b == '1':
            if c == '1': ans.append([n-2,n-1])
            if d == '1': ans.append([n-1,n-2])
        elif a == '1' and b == '0':
            if c == '1' and d == '1': ans.append([0,1])
            elif c == '1' and d == '0': ans = [[0,1],[n-1,n-2]]
            elif c == '0' and d == '1': ans = [[0,1],[n-2,n-1]]
            elif c == '0' and d == '0': ans.append([1,0])
        elif a == '0' and b == '1':
            if c == '1' and d == '1': ans.append([1,0])
            elif c == '1' and d == '0': ans = [[0,1],[n-2,n-1]]
            elif c == '0' and d == '1': ans = [[0,1],[n-1,n-2]]
            elif c == '0' and d == '0': ans.append([0,1])
        print(len(ans))
        for i in ans:
            print(i[0]+1,i[1]+1)

def C():
    s=input().rstrip()
    print(3)
    print('L',2)
    print('R',2)
    print('R',2*len(s)-1)

def D():
    def getCost(cost,x,y,c1,c2,c3,c4,c5,c6):
        h=min(x,y)
        if x > 0 and y > 0:
            cost += min(c1, c2+c6) * h
            x -= h
            y -= h
        if x < 0 and y > 0:
            cost += min([c3 + c2, c4 + 2 * c2, c1 + 2 * c3]) * h
            x += h
            y -= h
        elif x > 0 and y < 0:
            cost += min([c6 + c5, c4 + 2 * c6, c1 + 2 * c5]) * h
            x -= h
            y += h
        if x < 0:
            cost += min(c3, c4 + c2) * x * -1
        elif x > 0:
            cost += min(c6, c1 + c5) * x
        if y < 0:
            cost += min(c5, c4 + c6) * -1 * y
        elif y > 0:
            cost += min(c2, c1 + c3) * y
        return cost
    t=int(input())    
    for _ in range(t):
        x,y=map(int,input().split())
        #c1=(1,1)   c2=(0,1)    c3=(-1,0)
        #c4=(-1,-1) c5=(0,-1)   c6=(1,0)
        c1,c2,c3,c4,c5,c6=map(int,input().split())
        cost = 0
        h=min(abs(x),abs(y))
        if x < 0 and y < 0:
            c1,c4,c2,c5,c3,c6=c4,c1,c5,c2,c6,c3
            x,y=x*-1,y*-1
        if x > 0 and y > 0:
            c12 = min([c1 + c2, 2 * c2 + c4, 2 * c1 + c5])
            c21 = min([c1 + c6, 2 * c1 + c3, c2 + 2 * c6])
            if x >= 2 * y:
                cost = min([getCost(cost+c12*(x-y//2),x-y//2,y%2,c1,c2,c3,c4,c5,c6),
                           getCost(cost+c21*y,x-2*y,0,c1,c2,c3,c4,c5,c6),
                           getCost(cost,x,y,c1,c2,c3,c4,c5,c6)])
            elif y >= 2 * x:
                cost = min([getCost(cost+c12*x,0,y-2*x,c1,c2,c3,c4,c5,c6),
                           getCost(cost+c21*(y-x//2),x%2,y - x//2,c1,c2,c3,c4,c5,c6),
                           getCost(cost,x,y,c1,c2,c3,c4,c5,c6)])
            else:
                cost = min([getCost(cost+c12*(x-y//2),x - y//2,y%2,c1,c2,c3,c4,c5,c6),
                           getCost(cost+c21*(y-x//2),x%2,y - x//2,c1,c2,c3,c4,c5,c6),
                           getCost(cost,x,y,c1,c2,c3,c4,c5,c6)])
        else:
            cost=getCost(cost,x,y,c1,c2,c3,c4,c5,c6)
        print(cost)

def betterD():
    t=int(input())    
    for _ in range(t):
        x,y=map(int,input().split())
        #c1=(1,1)   c2=(0,1)    c3=(-1,0)
        #c4=(-1,-1) c5=(0,-1)   c6=(1,0)
        c1,c2,c3,c4,c5,c6=map(int,input().split())
        if x < 0 and y < 0:
            c1,c4,c2,c5,c3,c6=c4,c1,c5,c2,c6,c3
            x,y=x*-1,y*-1
        if y <= 0:
            y=abs(y)
            print(min([c6*x+c5*y,c5*(x+y)+c1*x,c6*(x+y)+c4]))
        elif x <= 0:
            x=abs(x)
            print(min([c2*y+c3*x,c3*(x+y)+c1*y,c2*(x+y)+c4]))
        else:
            if y > x: x,y=y,x
            print(min([c6*(x-y)+c1*y,c6*x+c2*y,c1*x+c3*(x-y)]))            
betterD()
