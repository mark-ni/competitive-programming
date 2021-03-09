from sys import stdout
s=list(input())

i,j=0,len(s)-1
l=set()
while i < j:
    if s[i] == '(':
        while j > i and s[j] == '(':
            j -= 1
        if j > i:
            l.add(i)
            l.add(j)
            i += 1
            j -= 1
    else:
        i += 1
if len(l) == 0:
    print(0)
else:
    print(1)
    print(len(l))
for i in sorted(list(l)):
    stdout.write(str(i + 1) + " ")

            
        
    
