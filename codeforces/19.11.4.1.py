n = int(input())

for i in range(n):
    li = [int(x) for x in input().split(' ')]
    a = li[0]
    b = li[1]
    n = li[2]
    s = li[3]

    if s - a * n > 0:
        s -= a * n
    else:
        s %= n
    if s <= b:
        print("YES")
    else:
        print("NO")
