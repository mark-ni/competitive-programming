from sys import stdin
input = stdin.readline
 
n = int(input())
amtLeft = 2*n
tot = 0
 
mins = [0]*(n)
maxs = [0]*(n)
index = 0
 
for i in range(n):
    flag = True
    li = list(map(int, input().split(' ')))
    nl = li[0]
    for i in range(2, nl+1):
        if li[i] - li[i-1] > 0:
            tot += amtLeft - 1
            amtLeft -= 2
            flag = False
            break
    if flag:
        a = li[1]
        b = li[nl]
        mins[index] = b
        maxs[index] = a
        index += 1

mins = sorted(mins[:index])
maxs = sorted(maxs[:index])

k = 0
for mi in range(index):
    m = mins[mi]
    while maxs[k] <= m and k < index-1:
        k+=1
    if maxs[k] == m:
        break
    tot += (index - k)
    
print(tot)        
    
              
    
