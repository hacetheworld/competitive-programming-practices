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


def _getPrime(N):
    primes = _sieve(N)
    result = []
    for i in range(len(primes)):
        if primes[i]:
            result.append(i)
    return result


def _primeFactor(N):
    primes = _getPrime(round(math.sqrt(N))+1)
    count = 0
    primeFactorRes = []
    for prime in primes:
        if N % prime == 0:
            count += 1
            primeFactorRes.append([prime, 0])
        while(N % prime) == 0:
            N = N//prime
            primeFactorRes[-1][1] += 1

    return primeFactorRes


def _NumberOfDivisor(N):
    primeFactors = _primeFactor(N)
    res = 1
    for primeFactor in primeFactors:
        res *= (primeFactor[1]+1)
    return res


N = int(input())
result = _primeFactor(N)
print(result)
print(_NumberOfDivisor(N))
