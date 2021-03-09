ol=int(input())
s=[ord(x)-ord('a') for x in input()]
t=sorted(s,reverse=True)
for i in t:
    l=len(s)
    if l==1:break
    for j in range(l):
        if s[j] == i:
            if j==0:
                if abs(s[1]-i)==1:
                    s.pop(j)
                    break
            elif j==l-1:
                if abs(s[l-2]-i)==1:
                    s.pop(j)
                    break
            elif abs(s[j-1]-i)==1 or abs(s[j+1]-i)==1:
                s.pop(j)
                break
print(ol-len(s))
