from sys import stdin
input=stdin.readline

for _ in range(int(input())):
    n=int(input())
    s1=sorted(list(map(int,input().split())))
    s2=sorted(list(map(int,input().split())))
    print(*s1)
    print(*s2)
