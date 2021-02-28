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


def Solution(arr, n):
    arr = sorted(arr, key=lambda x: x[-1], reverse=True)
    prefixSum = [0]
    for v in arr:
        prefixSum.append(prefixSum[-1]+v[1])
    prefixSum.pop(0)
    pair = [-1, -1]
    for v in arr:
        if v[0] > pair[0]:
            pair[0] = v[0]
            pair[1] = v[1]
    print(float(min(pair[0], pair[1]+(prefixSum[-1]-pair[1])//2)), end=" ")
    for k in range(2, n+1):
        tmp = 0
        el = 0
        for j in range(k):
            tmp += arr[j][1]
            el += arr[j][0]
        print(float(min(el, tmp+(prefixSum[-1]-tmp)//2)), end=" ")


def main():
    # //Write Your Code Here
    n = get_int()
    arr = get_list_of_list(n)
    Solution(arr, n)


#  calling main Function
if __name__ == "__main__":
    main()
