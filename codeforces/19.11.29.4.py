n = int(input())

values = [set([i]) for i in range(0, 26)]
keys = [i for i in range(0, 26)]
dicc = dict(zip(keys, values))
elementsAppeared = set([])
setsAppeared = []

def func(a):
    for x in a:
        for y in set(a):
            if y not in dicc[x]:
                for e in dicc[x]:
                    dicc[e] = dicc[x].union(dicc[y])
                dicc[y] = dicc[x]
        elementsAppeared.add(x)

for i in range(n):
    func(set([ord(x) - 97 for x in input()]))

for i in elementsAppeared:
    if dicc[i] not in setsAppeared:
        setsAppeared.append(dicc[i])

print(len(setsAppeared))
