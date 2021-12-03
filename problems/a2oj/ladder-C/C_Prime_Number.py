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


def power(a, b, mod):
    res = 1
    while b > 0:
        if b & 1:
            res = (res*a) % mod
        a = (a*a) % mod
        b = b//2
    return res
# -------------- SOLUTION FUNCTION ------------------


def Solution():
    # Write Your Code Here
    n, x = get_ints_in_variables()
    arr = get_ints_in_list()
    mod = pow(10, 9)+7
    s = 0
    t = power(x, sum(arr), mod)
    # print(t)
    for v in arr:
        d = power(x, v, mod)
        s += d
        s = s % mod
    # print(s)
    print(math.gcd(t-s, t) % mod)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
