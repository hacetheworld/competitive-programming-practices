# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

# -------- IMPORTANT ---------#
# SUN BHOS**KE AGAR MERA TEMPLATE COPY KAR RHA HAI NA TOH KUCH CHANGES BHI KAR DENA ESS ME, VARNA MUJEHY WARNING AAYEGI BAAD ME, PLEASE YAAR KAR DENA, OK :).
import sys
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


def get_int(): return int(input())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()


def canWin(arr, prefix, n, mid):
    s = prefix[mid+1]
    for i in range(mid+1, n):
        if s >= arr[i][0]:
            s += arr[i][0]
        else:
            break
    if s >= prefix[-1]:
        return True
    else:
        return False


def Solution(arr, n):
    l = 0
    r = n-1
    a = sorted([[arr[i], i+1] for i in range(n)], key=lambda x: x[0])
    prefix = [0]
    for v in a:
        prefix.append(prefix[-1]+v[0])

    ans = -1
    # print(prefix)
    while l <= r:
        mid = (l+r)//2

        if canWin(a, prefix, n, mid):
            ans = mid
            r = mid-1
        else:
            l = mid+1
    if ans == -1:

        print(n)
        for v in range(1, n+1):
            print(v, end=" ")
        print()
        return
    else:
        print(n-(ans))
        res = []
        for v in range(ans, n):
            res.append(a[v][1])
        res = sorted(res)
        for v in res:
            print(v, end=" ")
        print()


def main():
    # //Write Your Code Here
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


#  calling main Function
if __name__ == "__main__":
    main()
