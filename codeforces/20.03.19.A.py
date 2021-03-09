from sys import stdout
t=int(input())
for _ in range(t):
    n=int(input())
    if n==1:
        stdout.write('-1')
    else:
        stdout.write('76')
        stdout.write('7'*(n-2))
    stdout.write('\n')
    
