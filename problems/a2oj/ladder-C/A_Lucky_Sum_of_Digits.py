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
    sevens = n//7
    sevenRem = n % 7
    fours = sevenRem//4
    foursRem = sevenRem % 4
    if foursRem <= sevens:
        sevens -= foursRem
        fours += (2*foursRem)
        for _ in range(fours):
            print(4, end="")
        for _ in range(sevens):
            print(7, end="")
        print()
    else:
        print(-1)


def main():
    # Take input Here and Call solution function
    Solution(get_int())


# calling main Function
if __name__ == '__main__':
    main()
