n = int(input())

digs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def replace(string, index, char):
    string += " "
    s = string[0:index] + char + string[index+1:]
    return s.rstrip()

def getAns(k):
    pins = []
    newpins = []
    count = 0

    for j in range(k):
        pins.append(input())

    for a in range(k):
        flag = False
        theSet = set(pins).union(newpins)

        if pins[a] not in newpins:
            newpins.append(pins[a])
        else:
            for b in range(4):
                for c in range(10):
                    x = replace(pins[a], b, digs[c])
                    if x not in theSet:
                        newpins.append(x)
                        count += 1
                        flag = True
                        break
                if flag:
                    break
    print(count)
    for thing in newpins:
        print(thing)
    

for i in range(n):
    getAns(int(input()))