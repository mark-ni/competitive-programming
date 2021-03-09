t = int(input())
for i in range(t):
    n = int(input())
    s = []
    if n % 2 == 1:
        s.append('7')
        n -= 3
    while n > 0:
        s.append('1')
        n -= 2
    print(''.join(s))

        
