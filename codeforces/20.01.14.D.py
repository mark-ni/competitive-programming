from sys import stdin
input = stdin.readline

n,m=map(int,input().split(' '))
l=[0]*n*m
for i in range(n):
    l[m*i:m*i+m]=list(map(int,input().split(' ')))
currMaxMin = 0
ind1 = -1
ind2 = -1
for i in range(0,m*n,m):
    for j in range(i + m, m*n, m):
        currMin = 10**9
        flag = True
        #print(str(l[i:i+m]))
        #print(str(l[j:j+m]))
        #print()
        for k in range(m):
            a = max(l[i+k],l[j+k])
            #print(a)
            if a < currMaxMin:
                flag = False
                break
            if a < currMin:
                currMin = a
        if currMin > currMaxMin:
            if flag:
                currMaxMin = currMin
                ind1 = (i//m) + 1
                ind2 = (j//m) + 1
                #print("success")
print(*[ind1,ind2])
                
        
    
