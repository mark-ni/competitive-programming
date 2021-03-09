#started 12:47
import sys

s = input()

seqs = []
prod = 1

ustreak = 0
nstreak = 0
for i in range(len(s)):
    if s[i] == 'u':
        ustreak += 1
    else:
        if ustreak > 1:
            seqs.append(ustreak)
        ustreak = 0

    if s[i] == 'n':
        nstreak += 1
    else:
        if nstreak > 1:
            seqs.append(nstreak)
        nstreak = 0
    
    if s[i] == 'w':
        prod = 0
        break
    if s[i] == 'm':
        prod = 0
        break
if ustreak > 1:
    seqs.append(ustreak)
elif nstreak > 1:
    seqs.append(nstreak)

for i in seqs:
    prod *= i
print(prod % (10**9 + 7))
    
