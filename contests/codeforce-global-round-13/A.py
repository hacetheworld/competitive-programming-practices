# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

# import inbuilt standard input output
import sys
import heapq
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


def Solution():
    pass


def main():
    # //Write Your Code Here
    n, q = get_ints_in_variables()
    arr = sorted(get_ints_in_list(), reverse=True)
    oneRange = [0, 0]
    zeroRange = [0, 0]
    if arr[0] == 0:
        zeroRange[0] = 0
        zeroRange[1] = n-1
    elif arr[-1] == 0:
        oneRange[0] = 0
        for i in range(n):
            if arr[i] == 0:
                oneRange[1] = i-1
                zeroRange[0] = i
                break
        zeroRange[1] = n-1
    elif arr[-1] == 1:
        oneRange[0] = 0
        oneRange[1] = n-1
    for _ in range(q):
        t, qr = get_ints_in_variables()
        mn = 1 if oneRange[0] <= qr-1 and qr-1 <= oneRange[1] else 0
        if t == 1:
            if 1-mn == 0:
                oneRange[1] -= 1
                zeroRange[0] -= 1
            else:
                oneRange[1] += 1
                zeroRange[0] += 1
        else:
            print(mn)


#  calling main Function
if __name__ == "__main__":
    main()
