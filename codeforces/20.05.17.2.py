from sys import stdin
input=stdin.readline

def A():
    li=[]
    for i in range(2, 30):
        li.append(2**i - 1)
    for _ in range(int(input())):
        n=int(input())
        j=0
        while j<len(li):
            if n % li[j] == 0:
                print(n//li[j])
                break
            j += 1
    return

def B():
    for _ in range(int(input())):
        n=int(input())
        if n//2 % 2 == 1: print("NO")
        else:
            print("YES")
            arr=[0]*n
            for i in range(1,n//2+1): arr[i-1]=2*i
            for i in range(n//2, n-1): arr[i]=2*(i-n//2)+1
            arr[n-1] = sum(arr[:n//2])-sum(arr[n//2:])
            print(*arr)
    return

def C():
    from collections import deque
    for _ in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        pos=False
        if a[0] > 0: pos=True
        curr=a[0]
        tot=0
        for i in range(n):
            if a[i] > 0:
                if not pos:
                    tot += curr
                    pos=True
                    curr=a[i]
                else:
                    curr=max(a[i],curr)
            else:
                if pos:
                    tot += curr
                    pos=False
                    curr=a[i]
                else:
                    curr=max(a[i],curr)
        tot += curr
        print(tot)
    return

def D():
    return

def E():
    return

C()
