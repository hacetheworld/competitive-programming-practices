maxInt = 100000


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
    return primeNumbers


primes = sieve(maxInt)


def neareastPrime(N):
    l, r = N-1, N+1
    if l <= 2:
        return 1
    while True:

        if isPrime(l):
            return l
        elif isPrime(r):
            return r
        else:
            l -= 1
            r += 1


def isPrime(a):
    return primes[a]


for t in range(int(input())):
    N = int(input())
    print(neareastPrime(N))
