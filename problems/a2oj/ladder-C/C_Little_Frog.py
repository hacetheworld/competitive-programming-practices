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


def Solution(n):
    # Write Your Code Here
    l = 1
    r = n
    pos = 0
    while l <= r:
        if pos % 2 == 0:
            print(r, end=" ")
            r -= 1
        else:
            print(l, end=" ")
            l += 1
        pos += 1
    print()


def main():
    # Take input Here and Call solution function
    Solution(get_int())


# calling main Function
if __name__ == '__main__':
    main()
