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


def calc(a, b, c):
    return a[1]+b[1]+c[1]


def Solution(s, c, n):
    # Write Your Code Here
    # a=[-1,-1]
    # b=[-1,-1]
    # c=[-1,-1]
    # ans = 0
    # for i in range(n):
    #     if c[i]<a[i][1]:
    pass


def main():
    # Take input Here and Call solution function
    n = get_int()
    s = get_ints_in_list()
    c = get_ints_in_list()
    Solution(s, c, n)


# calling main Function
if __name__ == '__main__':
    main()
