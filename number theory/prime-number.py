# _Sieve of erthonisis(I know it's wrong spelleing)
# time complexity is N log(log(n))
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


def _primeCount(N):
    primes = _sieve(N)
    count = 0
    for isPrime in primes:
        if isPrime:
            count += 1
    return count


N = int(input())
print(_getPrime(N))
