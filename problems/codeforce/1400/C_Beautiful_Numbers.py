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


def factorial(fact, n, mod):
    for i in range(1, n+1):
        fact[i] = ((i % mod) * (fact[i-1]) % mod) % mod


def ncr(fact, n, r, mod):
    if r > n | n < 0 | r < 0:
        return 0
    return (fact[n] % mod)*(power(fact[r], mod-2, mod) % mod)*(power(fact[n-r], mod-2, mod) % mod) % mod


def Solution(a, b, n, fact, mod):
    # Write Your Code Here
    res = 0
    for i in range(n+1):
        t = (a*i)+((n-i)*b)
        flag = False
        while t > 0:
            if t % 10 != a and t % 10 != b:
                flag = True
                break
            t = t//10
        if flag:
            continue
        res = (res % mod + ncr(fact, n, i, mod) % mod) % mod
    print(res)


def main():
    # Take input Here and Call solution function
    mod = 1000000007
    a, b, n = get_ints_in_variables()
    fact = [1 for _ in range(n+1)]
    factorial(fact, n, mod)
    Solution(a, b, n, fact, mod)


# calling main Function
if __name__ == '__main__':
    main()
