# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

# -------- IMPORTANT ---------#
# SUN BHOS**KE AGAR MERA TEMPLATE COPY KAR RHA HAI NA TOH KUCH CHANGES BHI KAR DENA ESS ME, VARNA MUJEHY WARNING AAYEGI BAAD ME, PLEASE YAAR KAR DENA, OK :).
import sys
import bisect
from bisect import bisect_right

import math
from sys import stdin, stdout

# //Most Frequently Used Number Theory Concepts
# VAISE MEIN JAYDA USE KARTA NHI HU ENHE BUT COOL BANNE KE LIYE LIKH LEYA TEMPLATE ME VARNA ME YE TOH DUSRI FILE MAI SE BHI COPY PASTE KAR SAKTA THA :).


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

# TAKE INPUT
# HAAN YE BHUT KAAM AATA HAI INPUT LENE ME


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()


def factorial(n, m):
    if n == 1:
        return 1
    return (n % m*factorial(n-1, m) % m) % m


def Solution(s, m):
    n = len(s)
    f = factorial(n, m)
    hm = {}
    for c in s:
        if c in hm:
            hm[c] += 1
        else:
            hm[c] = 1
    tmp = 1
    for v in hm:
        if hm[v] > 1:
            tmp = (tmp % m * factorial(hm[v], m) % m) % m
    print(round(f/tmp))


def main():
    # //Write Your Code Here
    m = pow(10, 9)+7
    for _ in range(get_int()):
        s = get_string()
        Solution(s, m)


#  calling main Function
if __name__ == "__main__":
    main()
