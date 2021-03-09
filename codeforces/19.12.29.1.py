t = int(input())

for _ in range(t):
    n, k1, k2 = map(int, input().split(' '))
    l1 = list(map(int, input().split(' ')))
    l2 = list(map(int, input().split(' ')))
    if n in l1:
        print("YES")
    else:
        print("NO")
