t=int(input())
for _ in range(t):
    n,days=map(int,input().split())
    a=list(map(int,input().split()))
    i = 1
    while i < n:
        if a[i] > 0:
            if days - i >= 0:
                days -= i
                a[i] -= 1
                a[0] += 1
            else:
                break
        else:
            i += 1
    print(a[0])
            
        
