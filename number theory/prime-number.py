# Sieve of erthonisis(I know it's wrong spelleing)
def sieve(N):
    primeNumbers = [True]*(N+1)
    primeNumbers[0] = False
    primeNumbers[1] = False
    i = 2
    while i*i <= N:
        j = i
        if primeNumbers[j]:
            while j*i <= N:
                primeNumbers[j*i] = False
                j += 1
        i += 1
    count = 0
    for isPrime in (primeNumbers):
        if isPrime:
            count += 1
    print(count)


N = int(input())
sieve(N)
