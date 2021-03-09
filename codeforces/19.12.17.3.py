from sys import stdout

x = [int(x) for x in input().split(' ')]
r = x[0]
c = x[1]

def getAns(c, r):
    rli = []
    cli = []
    if r < c:
        rli = list(range(2, 2*r + 2, 2))
        cli = [2] + list(range(3, 2*r, 2))
        cli.extend(list(range(2*r + 1, r + c + 1)))
    else:
        cli = list(range(2, 2*c + 2, 2))
        rli = [2] + list(range(3, 2*c, 2))
        rli.extend(list(range(2*c + 1, r + c + 1)))

    if r == 1 and c == 1:
        print(0)
    else:
        stdout.write('2')
        for k in range(1, r):
            stdout.write(' ')
            stdout.write(str(rli[k]))
        stdout.write('\n')
        for i in range(1, c):
            stdout.write(str(cli[i]))
            for j in range(1, r):
                stdout.write(' ')
                stdout.write(str(cli[i] * rli[j]))
            if not i == c - 1:
                stdout.write('\n')

getAns(r, c)
