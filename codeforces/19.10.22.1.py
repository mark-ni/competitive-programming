n = int(input())
for i in range(n):
    m = int(input())
    li = sorted([int(x) for x in input().split(' ')])
    final = 1
    for j in range(1, len(li)):
        if li[j] - li[j -1] == 1:
            final += 1
            break
    print(final)