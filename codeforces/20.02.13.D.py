from sys import stdout
def getAns(n,m,k):
    if (4 * n * m - 2 * n - 2 * m >= k):
        stdout.write("NO\n")
        return
    stdout.write("YES\n")
    seqs = ['']*3000
    lenseq = 0
    beginningInstruc = ['R']*(m - 1) + ['L']*(m - 1)
    bl = len(beginningInstruc)
    middleInstruc = (['D'] + ['R','U','D']*(m - 1)) + ['L'] * (m - 1)
    ml = len(middleInstruc)
    endInstruc = ['U'] * (n - 1)
    el = len(endInstruc)
    if (len(beginningInstruc)) > k:
        if k >= (m - 1):
            seqs.append([str(m-1) + ' R'])
            seqs.append([str(k - m + 1) + ' L'])
        else:
            seqs.append([str(k) + ' R'])
        return seqs
    else:
        seqs.append([str(m - 1) + ' R'])
        seqs.append([str(k - m + 1) + ' L'])
    currInd = bl
    for i in range(n - 1):
        if currInd + ml > k:
            if (k - currInd) >= 1:
                seqs.append(['1 D'])
                if (k - currInd) >= (m):
                    seqs.append([str(m - 1) + ' RUD'])
                    if (k - currInd) >= ml:
                        seqs.append(
                elif k > 1:
                    seqs.append([str(k - 1 - currInd) + ' RUD'])

            return moves
        else:
            seqs.append(['1 D'])
            seqs.append([str(m - 1) + ' RUD'])
            seqs.append([str(m - 1) + ' L'])
        currInd += ml
    moves[currInd:k] = endInstruc[0:k-currInd]
    return moves

n,m,k=map(int,input().split())
li = getAns(n,m,k)
currChar = ''
currCount = 0
for i in range(len(li)):
    

