from sys import stdin,stdout
input=stdin.readline
def getAns():
    N=int(input())
    l=[]
    s=''
    starts=[]
    ends=[]
    middles=[]
    for i in range(N):
        q=input().rstrip().split('*')
        starts.append(q[0])
        ends.append(q[len(q)-1][::-1])
        for j in range(1,len(q)-1):
            middles.append(q[j])
    start=''
    for i in starts:
        for j in range(min(len(start),len(i))):
            if start[j] != i[j]:
                return '*'
        if len(i) > len(start):
            start += i[len(start):]
    end=''
    for i in ends:
        for j in range(min(len(end),len(i))):
            if end[j] != i[j]:
                return '*'
        if len(i) > len(end):
            end += i[len(end):]
    return start + ''.join(middles) + end[::-1]

    
T=int(input())
for _ in range(T):
    s=getAns()
    stdout.write('Case #' + str(_+1) + ': ')
    stdout.write(s)
    stdout.write('\n')
            
        
            
        
