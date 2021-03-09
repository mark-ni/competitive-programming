while True:
  lastUL = lastUL + 4 * rL + 2
  lastUR = lastUR + 4 * rL + 4
  lastDL = lastDL + 4 * rL
  lastDR = lastDR + 4 * rL - 2

  rL += 2

  runningTot = 1
  runningPrimes = 1

  for num in [lastUL, lastUR, lastDL, lastDR]:
    if isPrime(num):
      runningPrimes += 1
  runningTot += 4

  if runningPrimes / runningTot <= 10:
    print(rL)
    break
