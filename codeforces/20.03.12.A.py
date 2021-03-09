for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    mod=a[0]%2
    flag=True
    for i in a:
        if i%2 != mod:
            flag=False
            break
    if flag: print("YES")
    else: print("NO")
