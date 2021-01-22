import math


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


def findPrime(primes, frm):
    for p in range(frm, len(primes)):
        if primes[p]:
            return p


def Solution(primes, d):
    # Solution
    a = findPrime(primes, 1+d)
    b = findPrime(primes, a+d)
    return a*b


primes = sieve(pow(10, 5))
for t in range(int(input())):
    N = int(input())
    # arr = list(map(int, input().split()))
    # strArr = [input() for _ in range(N)]
    print(Solution(primes, N))
