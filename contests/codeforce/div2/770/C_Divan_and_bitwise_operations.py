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


def power(a, b, mod):
    res = 1
    while b > 0:
        if b & 1:
            res = (res*a) % mod
        a = (a*a) % mod
        b = b//2
    return res


def Solution():
    # Write Your Code Here
    pass


def main():
    # Take input Here and Call solution function
    mod = pow(10, 9)+7
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        xr = 0
        for _ in range(m):
            l, r, x = get_ints_in_variables()
            xr |= x
        ans = ((power(2, n-1, mod) % mod)*(xr % mod)) % mod
        print(ans)


# calling main Function
if __name__ == '__main__':
    main()
