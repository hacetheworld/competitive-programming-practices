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


def Solution(a, n, e, isPrime):
    # Write Your Code Here
    ans = 0
    for i in range(n):
        if not isPrime[a[i]]:
            continue
        l = 0
        r = 0
        j = i+e
        while j < n:
            if a[j] == 1:
                l += 1
            else:
                break
            j += e

        j = i-e
        while j >= 0:
            if a[j] == 1:
                r += 1
            else:
                break
            j -= e
        ans += ((l*r)+l+r)
    print(ans)


def main():
    # Take input Here and Call solution function
    isPrime = sieve(pow(10, 6)+1)
    for _ in range(get_int()):
        n, e = get_ints_in_variables()
        a = get_ints_in_list()
        Solution(a, n, e, isPrime)


# calling main Function
if __name__ == '__main__':
    main()
