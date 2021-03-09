t=int(input())
for _ in range(t):
    n=int(input())
    tot=0
    while n >= 2:
        k=2*n
        s=int((k/3)**(1/2))
        while (s/2 + 3/2 * s * s) < n:
            s += 1
        while (s/2 + 3/2 * s * s) > n:
            s -= 1
        n-=int(s/2 + 3/2 * s * s)
        tot+=1
    print(tot)
