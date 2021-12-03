# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout

# -------------- INPUT FUNCTIONS ------------------


def get_ints_in_variables(): return map(
    int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# -------- SOME CUSTOMIZED FUNCTIONS-----------


def myceil(x, y): return (x + y - 1) // y

# -------------- SOLUTION FUNCTION ------------------


def sieve(N, cnt, el, idx):
    primeNumbers = [True]*(N+1)
    primeNumbers[0] = False
    primeNumbers[1] = False
    i = 3
    while i*i <= N:
        j = i
        if primeNumbers[j]:
            while j*i <= N:
                if el[j*i] > 0:
                    cnt[idx] += 1
                primeNumbers[j*i] = False
                j += 1
        idx += 1
        i += 1
    # res = []
    # for i in range(len(primeNumbers)):
    #     if primeNumbers[i]:
    #         res.append(i)
    # return primeNumbers


def nearPrime(primes, t, f):
    if f == 0:
        for v in primes:
            if v >= t:
                return v
        # return primes[-1]
    else:
        for i in range(len(primes)-1, -1, -1):
            if primes[i] <= t:
                return primes[i]
        return 2


def Solution(arr, n):
    # Write Your Code Here
    cnt = [0 for _ in range(max(arr)+1)]
    elements = [0 for _ in range(max(arr)+1)]
    for v in arr:
        if v % 2 == 0:
            cnt[1] += 1
        elements[v] += 1
    pre = [0 for _ in range(max(arr)+1)]
    sieve(max(arr)+1, cnt, elements, 2)
    t = max(arr)
    # print(pref)
    pref.pop(0)
    for _ in range(get_int()):
        l, r = get_ints_in_variables()
        if r > t:
            r = t
        if l > t:
            l = t
        print(pref[r]-pref[l-1])


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_ints_in_list()
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
