from sys import stdin
s=[ord(x) - ord('a') for x in input().rstrip()]

alphabet = [[0 for i in range(26)] for j in range(26)]
currSeen = [0]*26
for i in s:
    for j in range(26):
        if currSeen[j] > 0:
            alphabet[j][i] += currSeen[j]
    currSeen[i] += 1
for i in range(26):
    alphabet[i] = max(alphabet[i])

print(max(max(alphabet),max(currSeen)))
