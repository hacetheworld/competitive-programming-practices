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


def Solution(a, b, c, n, m):
    g = [[] for _ in range(n+1)]
    for i in range(n):
        if a[i] != b[i]:
            g[b[i]].append(i)
    last = -1
    if len(g[c[-1]]) > 0:
        last = g[c[-1]][-1]
        g[c[-1]].pop()
    else:
        for i in range(n):
            if b[i] == c[-1]:
                last = i
                break
    if last == -1:
        print("NO")
        return
    ans = [0 for _ in range(m+1)]
    ans[m-1] = last
    for i in range(m-1):
        if len(g[c[i]]) == 0:
            ans[i] = last
        else:
            ans[i] = g[c[i]][-1]
            g[c[i]].pop()
    for i in range(1, n+1):
        if len(g[i]) > 0:
            print("NO")
            return
    print("YES")
    for i in range(m):
        print(ans[i]+1, end=" ")
    print()


def main():
    # //Write Your Code Here
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        a = get_ints_in_list()
        b = get_ints_in_list()
        c = get_ints_in_list()
        Solution(a, b, c, n, m)


#  calling main Function
if __name__ == "__main__":
    main()
