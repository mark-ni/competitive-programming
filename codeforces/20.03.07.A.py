def getAns(n,a):
    if n==1:
        if a[0] % 2 == 0: print('1\n1')
        else: print('-1')
        return
    if a[0] % 2 == 0: print('1\n1')
    elif a[1] % 2 == 0: print('1\n2')
    else: print('2\n1 2')
        
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    getAns(n,a)
