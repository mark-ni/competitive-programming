def getAns(n):
    l = [0]*int(math.ceil(math.sqrt(n))+1)    

    while n%2==0:
        l[2]+=1
        n//=2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n%i==0:
            l[i]+=1
            n//=i
    if n > 2:
        print('1 ' + str(n))
        return
    li = []
    for i in range(len(l)):
        if l[i] > 0:
            li.append(i**(l[i]))
    currentmin = n
    for i in range(len(li)):
        
        
    
        


n = int(input())
getAns(n)
