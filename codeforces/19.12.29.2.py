for _ in range(int(input())):
    n,l=int(input()), list(map(int, input().split(' ')))
    s = sum(l)
    xor = l[0]
    for i in range(1, n): xor = l[i] ^ xor
    if s - (xor*2) == 0: print('0\n')
    else: print('2\n'+str(xor) + " " + str(xor+s))
    
    

