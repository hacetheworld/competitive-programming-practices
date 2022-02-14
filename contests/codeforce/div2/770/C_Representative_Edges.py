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


def isAirthmeticP(a, l, r):
    d = a[l+1]-a[l]
    for i in range(l+1, r):
        if abs(a[i+1]-a[i]) != d:
            return False
    return True


def Solution(a, n):
    # Write Your Code Here
    l, r = 0, 1

    for i in range(n):
        for j in range(i+1, n):
            if isAirthmeticP(a, i, j):
                if ((r-l)+1) < ((j-i)+1):
                    l, r = i, j
    d = abs(a[r]-a[r-1])
    for i in range(l, 0, -1):


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        a = get_ints_in_list()
        Solution(a, n)


# calling main Function
if __name__ == '__main__':
    main()
