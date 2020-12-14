def SieveOfEratosthenes(n, prime):
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1


n = 10000000
primes = [True for _ in range(n+1)]
primes[0] = False
primes[1] = False
SieveOfEratosthenes(n, primes)
for i in range(len(primes)):
    if primes[i]:
        print(i)
print(end="")
