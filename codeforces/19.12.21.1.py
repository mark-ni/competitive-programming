n = int(input())
a = 0
b = 0
if n % 2 == 0:
    a = n + 4
    b = 4
else:
    if n % 3 == 0:
        a = n + 6
        b = 6
    elif n % 3 == 1:
        a = n + 8
        b = 8
    else:
        a = n + 4
        b = 4
string = str(a) + " " + str(b)
print(string)
        
