from sys import stdin,stdout
input=stdin.readline

def p(r,k):
    stdout.write(str(r) + ' ' + str(k) + '\n')

def getAns(n):
    if n == 1:
        return
    stdout.write('2 2\n')
    if n == 2:
        return
    r,k=2,2
    s=2
    while s + r < n:
        s += r
        r += 1
        p(r,k)
    k -= 1
    while s != n:
        p(r,k)
        r += 1
        s += 1

T=int(input())
for _ in range(T):
    n=int(input())
    stdout.write('Case #' + str(_ + 1) + ':\n')
    stdout.write('1 1\n')
    getAns(n)
        
        
        
    
        
    
    
