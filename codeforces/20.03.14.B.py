from sys import stdin
input=stdin.readline
t=int(input())
for _ in range(t):
    n = int(input())
    a=set(map(int,input().split()))
    print(len(a))
