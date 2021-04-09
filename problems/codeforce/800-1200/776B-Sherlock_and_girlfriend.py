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


def countColor(N):
    primes = sieve(pow(10, 6))
    if N > 2:
        print("2")
    else:
        print("1")
    print(end="")
    for i in range(2, N+2):
        if primes[i]:
            print("1", end=" ")
        else:
            print("2", end=" ")
    # print(end="")


N = int(input())
countColor(N)
