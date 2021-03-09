n,m = map(int,input().split(' '))
a = list(input().split(' '))
b = list(input().split(' '))
q = int(input())
for i in range(q):
    y = int(input()) - 1
    print(a[y%n] + b[y%m])
    
