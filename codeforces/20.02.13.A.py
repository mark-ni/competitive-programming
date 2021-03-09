t = int(input())
for _ in range(t):
    a = list(input())
    b = list(input())
    c = list(input())
    flag = True
    for i in range(len(c)):
        if c[i] != a[i] and b[i] != c[i]:
            print("NO")
            flag = False
            break
    if flag:
        print("YES")
