cap = 20
li = [[0] * cap for i in range(cap)]

for row in range(cap):
    for col in range(cap):
        li[row][col] = 0

for row in range(cap):
    for col in range(cap):
        if row < col:
            li[row][col] = 0
        elif row == col or col == 0 or row - col == 1:
            li[row][col] = 1
        else:
            li[row][col] = 0
            increment = col + 1
            diff = row - col

            while (diff > 0):
                li[row][col] += sum(li[diff - 1][0:col])
                diff -= increment
                if diff == 0:
                    li[row][col] += 1
for row in li:
    print(str(li.index(row)+1) + ": " + str(sum(row)) + ":\t" + str(row) + "\n")
        
