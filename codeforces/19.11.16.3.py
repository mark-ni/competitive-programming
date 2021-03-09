l1 = [int(x) for x in input().split(' ')]
li2 = [int(y) for y in input().split(' ')]
li2.sort()

n = l1[0]
cap = l1[1]

tot = li2[0]
string = str(tot)

for m in range(2,n+1):
    tot += sum([li2[x] for x in range((m-1)%cap,m,cap)])
    string += ' ' + str(tot)

print(string)
    
