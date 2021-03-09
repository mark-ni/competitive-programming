t=int(input())
for _ in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    s=set(range(2 * n + 1))
    s.remove(0)
    l=[201]*(2*n)
    flag = True
    for i in range(0, 2*n, 2):
        l[i] = b[i//2]
        s.remove(l[i])
    for i in range(1, 2*n, 2):
        for num in s:
            if num > l[i - 1] and num < l[i]:
                l[i] = num
        if (l[i] == 201):
            print(-1)
            flag = False
            break
        s.remove(l[i])
    if flag:
        print(*l)
