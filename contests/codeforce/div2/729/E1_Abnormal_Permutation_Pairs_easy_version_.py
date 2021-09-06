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


def factorial(fact, n, mod):
    for i in range(1, n+1):
        fact[i] = ((i % mod) * (fact[i-1]) % mod) % mod


def Solution(n, mod):
    # Write Your Code Here
    fact = [1 for _ in range(n+1)]
    factorial(fact, n, mod)
    ans = ((fact[n-1]*(n-1)) % mod)-1
    print(ans)


def main():
    # Take input Here and Call solution function

    n, mod = get_ints_in_variables()
    Solution(n, mod)


# calling main Function
if __name__ == '__main__':
    main()
