import math


def _sieve(N):
    primes = [True]*(N+1)
    primes[0] = False
    primes[1] = False
    sqrtN = round(math.sqrt(N))
    for i in range(2, sqrtN+1):
        if primes[i]:
            for j in range(i*i, N+1, i):
                primes[j] = False
    return primes


def _printPrime(N):
    primes = _sieve(N)
    result = []
    for i in range(len(primes)):
        if primes[i]:
            result.append(i)
    return result


def _segmented_Sieve(L, R):
    primes = _printPrime(round(math.sqrt(R)))
    segmentArr = [True for _ in range(R-L+1)]
    for i in range(len(primes)):
        base = (L//primes[i])*primes[i]
        if base < L:
            base += primes[i]
        if L == 1 or L == 0:
            base = primes[i]
        for j in range(base, R+1, primes[i]):
            segmentArr[j-L] = False
        if base == primes[i]:
            segmentArr[base-L] = True
    result = []
    for k in range(len(segmentArr)):
        if segmentArr[k] and ((k+L) != 0 and (k+L) != 1):
            result.append(k+L)
    return result


L, R = map(int, input().split())
print(_segmented_Sieve(L, R))
