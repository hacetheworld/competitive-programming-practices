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


def Solution(arr, n, x, f):
    # Write Your Code Here
    ans = 0
    for v in arr:
        if v > x:
            tmp = (v//(f+x))
            if v % (f+x) > x:
                tmp += 1
            ans += (tmp*f)
    print(ans)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_ints_in_list()
    x, f = get_ints_in_variables()
    Solution(arr, n, x, f)


# calling main Function
if __name__ == '__main__':
    main()
