# import inbuilt standard input output
import sys
import math
from sys import stdin, stdout

# suppose a function called main() and
# all the operations are performed

# ////////// Get integer values in variables \\\\\\\\\\\\\\\\\\\\\\\


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_string(): return sys.stdin.readline().strip()


def factors(primes, tmp, n):
    for i in primes:
        if n < i:
            break
        if n % i == 0:
            while n % i == 0:
                tmp[i] += 1
                n = n//i
    if n > 1:
        tmp[n] = 1


def helper(primes, res, arr):
    tmp = [0 for _ in range(maxl)]
    for i in range(1, len(arr)):
        n = arr[i]
        factors(primes, tmp, n)
    for i in range(len(tmp)):
        res[i] = min(res[i], tmp[i])


maxl = 1000000


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


def main():
    # //TAKE INPUT HERE
    n = int(stdin.readline())
    primes = _getPrime(maxl)
    res = [float("inf") for _ in range(maxl)]
    # print(t)
    for _ in range(n):
        arr = get_ints_in_list()
        helper(primes, res, arr)
    r = 1
    for i in range(len(res)):
        if res[i] != 0:
            r *= pow(i, res[i])
    print(r)


# call the main method
if __name__ == "__main__":
    main()
