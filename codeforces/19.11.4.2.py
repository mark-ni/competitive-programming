n = int(input())

for i in range(n):
    length = int(input())
    s = set(list(range(1, length + 1)))
    li = [int(x) for x in input().split(' ')]
    k = 0
    while k < length - 1:
        nextIndex = li.index(min(s))
        if nextIndex == k:
            s.remove(li[k])
            k += 1
        else:
            temp = li[nextIndex]
            for i in range(k, nextIndex + 1):
                s.remove(li[i])
            li[k + 1:nextIndex + 1] = li[k:nextIndex]
            li[k] = temp
            k = nextIndex
            s.add(li[nextIndex])
    print(*li)
