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


def Solution(arr, n):
    # Write Your Code Here
    ans = n*n
    sm = []
    mx = []
    for v in arr:
        v = list(reversed(v[1:]))
        if sorted(v) == v:
            sm.append(v[0])
            mx.append(v[-1])
    sm = sorted(sm)
    mx = sorted(mx)
    for v in sm:
        pair = bisect.bisect(mx, v)
        ans -= pair
    print(ans)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_list_of_list(n)
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
