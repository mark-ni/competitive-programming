from sys import stdin,stdout
input=stdin.readline

n,m=map(int,input().split())
a=sorted(list(map(int,input().split())))
k=[a[0]] * n
for i in range(1, n):
    k[i] = k[i - 1] + a[i]
for i in range(m, n):
    k[i] += k[i - m]
for i in k:
    stdout.write(str(i))
    stdout.write(' ')
