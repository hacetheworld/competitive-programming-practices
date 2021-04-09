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

# -------------- SOLUTION FUNCTION ------------------


def power(a, b, mod):
    res = 1
    while b > 0:
        if b & 1:
            res = (res*a) % mod
        a = (a*a) % mod
        b = b//2
    return res


def Solution(arr, n):
    mod = 998244353
    # Write Your Code Here
    firstSum = 0
    for i in range(n):
        firstSum = (firstSum+arr[i]) % mod
    backSum = 0

    for i in range(2*n-1, n-1, -1):
        backSum = (backSum+arr[i]) % mod
    res = (backSum-firstSum) % mod
    # //Choose n element from  set of 2n elemnts
    fact = 1
    for i in range(1, n+1):
        res = (res*(n+i)) % mod
        fact = (fact*i) % mod
    res = (res*power(fact, mod-2, mod)) % mod
    print((res+mod) % mod)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = sorted(get_ints_in_list())
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
