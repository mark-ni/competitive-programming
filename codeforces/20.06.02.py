from sys import stdin
input=stdin.readline

for _ in range(int(input())):
    n,a,b,c,d=map(int,input().split())
    if (a-b)*n > (c+d) or (a+b)*n < (c-d): print("No")
    else: print("Yes")

    
