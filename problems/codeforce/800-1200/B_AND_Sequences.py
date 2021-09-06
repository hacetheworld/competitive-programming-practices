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


def Solution(a, n):
    # Write Your Code Here
    mod = pow(10, 9)+7
    andRes = a[0]
    for i in range(1, n):
        andRes &= a[i]
    cnt = 0
    for v in a:
        if v == andRes:
            cnt += 1
    if cnt <= 1:
        print(0)
    else:
        fact = 1
        for i in range(1, n-1):
            fact = (fact*i) % mod
        if n == 3:
            print((cnt*(cnt-1))*((n-2)) % mod)
        else:
            print((cnt*(cnt-1))*(fact) % mod)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        a = get_ints_in_list()
        Solution(a, n)


# calling main Function
if __name__ == '__main__':
    main()
