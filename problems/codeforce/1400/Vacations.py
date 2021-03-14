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


def helperFunc(arr, n, last, i, dp):
    if i >= n:
        return 0

    if dp[i][last] != 0:
        return dp[i][last]
    if arr[i] == 0:
        dp[i][last] = helperFunc(arr, n, 0, i+1, dp)+1
    elif arr[i] == 1:
        if last == 1:
            dp[i][last] = helperFunc(arr, n, 0, i+1, dp)+1
        else:
            dp[i][last] = helperFunc(arr, n, 1, i+1, dp)
    elif arr[i] == 2:
        if last == 2:
            dp[i][last] = helperFunc(arr, n, 0, i+1, dp)+1
        else:
            dp[i][last] = helperFunc(arr, n, 2, i+1, dp)
    else:
        a = float("inf") if last == 1 else helperFunc(arr, n, 1, i+1, dp)
        b = float("inf") if last == 2 else helperFunc(arr, n, 2, i+1, dp)
        dp[i][last] = min(a, b)

    return dp[i][last]


def Solution(arr, n):
    dp = [[0, 0, 0] for _ in range(105)]
    print(helperFunc(arr, n, 0, 0, dp))


def main():
    # //Write Your Code Here
    n = get_int()
    arr = get_ints_in_list()
    Solution(arr, n)


#  calling main Function
if __name__ == "__main__":
    main()
