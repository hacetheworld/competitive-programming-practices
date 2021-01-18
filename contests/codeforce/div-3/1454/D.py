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


def Solution(n):
    factors = sorted(_primeFactor(n), key=lambda x: -x[1])
    res = []
    # print(factors)
    if len(factors) > 0:
        for _ in range(factors[0][1]):
            res.append(factors[0][0])
        res[-1] *= (n//(pow(factors[0][0], factors[0][1])))
        print(len(res))
        for f in res:
            print(f, end=" ")
        print("")
    else:
        print(1)
        print(n)


for t in range(int(input())):
    N = int(input())
    # UnCOMMENT FOR TESTING IN VSCODE
    # print("<<<<<<<<<<<<<<<<-START->>>>>>>>>>>>>>>>>>>>")
    # Solution(N)
    # print("<<<<<<<<<<<<<<<<-END->>>>>>>>>>>>>>>>>>>>")
    # SUBMIT FOR SOLUTION
    Solution(N)
