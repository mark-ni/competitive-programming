n = int(input())
for _ in range(n):
    ki = int(input())
    k = list(input())

    streak = 0
    longest = 0
    isStreak = False
    for i in range(ki):
        if isStreak:
            if k[i] == 'P':
                streak += 1
            else:
                longest = max(streak, longest)
                streak = 0
        if k[i] == 'A':
            isStreak = True
    print(max(streak, longest))
