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


def power(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = (res*a)
        a = (a*a)
        b = b//2
    return res


def Solution():
    # Write Your Code Here
    k, b, n, t = get_ints_in_variables()
    if k == 1:
        z = n*b
        curr = t
        i = 0
        while curr < z:
            i += 1
            curr = t+i*b
        print(i)
        return
    mn = ((k*t)-t+b)//(k-1+b)
    tmp = power(k, n)
    i = 0
    while mn < tmp:
        i += 1
        tmp = power(k, (n-i))
    print(i)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
