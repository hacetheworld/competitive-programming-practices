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


def Solution(l, r):
    # Write Your Code Here
    ans = r-l
    d = 10
    while d <= r:
        a1 = l//d
        a2 = r//d
        ans += (a2-a1)
        d *= 10
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        l, r = get_ints_in_variables()
        Solution(l, r)


# calling main Function
if __name__ == '__main__':
    main()
