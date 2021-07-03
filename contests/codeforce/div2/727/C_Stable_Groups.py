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

# -------------- SOLUTION FUNCTION ------------------

# -------- SOME CUSTOMIZED FUNCTIONS-----------


def myceil(x, y):
    return (x + y - 1) // y


def Solution(arr, n, k, x):
    # Write Your Code Here
    arr = sorted(arr)
    differs = []
    for i in range(1, n):
        diff = arr[i]-arr[i-1]
        if diff > x:
            differs.append(diff)
    differs = sorted(differs)
    ans = len(differs)+1
    i = 0
    while k and i < len(differs):
        itm = differs[i]
        needVal = myceil(itm, x)-1
        k -= needVal
        if k < 0:
            break
        ans -= 1
        i += 1
    print(ans)


def main():
    # Take input Here and Call solution function
    n, k, x = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, k, x)


# calling main Function
if __name__ == '__main__':
    main()
