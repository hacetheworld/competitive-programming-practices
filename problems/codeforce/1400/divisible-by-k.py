# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

# import inbuilt standard input output
import sys
import math
from sys import stdin, stdout

# //Most Frequently Used Number Theory Concepts


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


def getPrime(N):
    primes = sieve(N)
    result = []
    for i in range(len(primes)):
        if primes[i]:
            result.append(i)
    return result


def factor(N):
    factors = []
    i = 1
    while i*i <= N:
        if N % i == 0:
            factors.append(i)
            if i != N//i:
                factors.append(N//i)
        i += 1
    return sorted(factors)


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def extendedGcd(a, b):
    if a < b:
        return extendedGcd(b, a)
    if b == 0:
        return [a, 1, 0]
    res = extendedGcd(b, a % b)
    x = res[2]
    y = res[1]-(math.floor(a/b)*res[2])
    res[1] = x
    res[2] = y
    return res


def iterativeModularFunc(a, b, c):
    res = 1
    while b > 0:
        if b & 1:
            res = (res*a) % c
        a = (a*a) % c
        b = b//2
    return res

# // Taking Input Format Helper Function


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_int(): return int(input())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()


def findPair(c, n, i, v):
    l = i+1
    r = n-1
    idx = -1
    while l <= r:
        mid = (l+r)//2
        if c[mid]+v > 0:
            idx = mid
            r = mid-1
        else:
            l = mid+1
    if idx == -1:
        return 0
    else:
        return n-idx


def Solution(a, n, k):
    a = sorted(a, reverse=True)
    x = 0
    res = 0
    print(a)
    for v in a:
        if (v+x) % k == 0:
            res = res+1
            x = x+1
        elif v % k != 0:
            if (v+x) <= k:
                addRem = k-v-x
                res = res+addRem+1
                x = x+addRem+1
            else:
                nextDivisbleNumber = math.ceil((v+x)/k)*k
                addRem = nextDivisbleNumber-v-x
                res = res+addRem+1
                x = x+addRem+1

    print(res)


def main():
    # //Write Your Code Here
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        a = get_ints_in_list()
        Solution(a, n, k)


#  calling main Function
if __name__ == "__main__":
    main()
