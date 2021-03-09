def ebne(s):
    while len(s) > 0 and s[len(s)-1] % 2 == 0:
        s.pop(len(s) - 1)
    while len(s) > 0 and s[0] == 0:
        s.pop(0)
    tot = sum(s)
    if tot % 2 == 1:
        for i in s:
            if i % 2 == 1:
                s.remove(i)
                break
    if len(s) == 0 or s[len(s) - 1] % 2 == 0:
        return -1
    elif s[0] == 0:
        return ebne(s)
    else:
        string = ''
        for i in s:
            string += str(i)
        return string

t = int(input())
for _ in range(t):
    n = int(input())
    s = [int(x) for x in input()]
    print(ebne(s))

