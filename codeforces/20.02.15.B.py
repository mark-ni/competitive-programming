#from sys import stdin
#input = stdin.buffer.readline

n,m=map(int,input().split())
currWord = []
currWords = []
for i in range(n):
    s = input()
    flag = True
    for word in currWords:
        if s == word[::-1]:
            currWord.append(word)
            currWords.remove(word)
            flag = False
            break
    if flag:
        currWords.append(s)


middleWordLength = 0
middleWord = ''
for i in currWords:
    if i == i[::-1]:
        middleWord = i
        middleWordLength = m
        break
print(m * len(currWord) * 2 + middleWordLength)
print(''.join(currWord) + middleWord + (''.join(currWord))[::-1])         
