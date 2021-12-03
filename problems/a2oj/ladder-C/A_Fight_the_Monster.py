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


def Solution():
    # Write Your Code Here
    yh, ya, yd = get_ints_in_variables()
    mh, ma, md = get_ints_in_variables()
    h, a, d = get_ints_in_variables()
    ans = float("inf")
    for ydr in range(210):
        for yat in range(123):
            if ya+ydr > md:
                if ma > yd+yat:
                    r = (mh+ya+ydr-md-1)//(ya+ydr-md)
                    y = r*(ma-yd-yat)+1
                    ans = min(ans, max(0, y
                                       - yh)*h+(ydr*a)+(yat*d))
                else:
                    ans = min(ans, (ydr*a)+(yat*d))
    print(ans)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
