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
    arr = sorted(arr)
    el = arr[0]
    cnt = 1
    for v in arr:
        if v != el:
            cnt += 1
            el = v
    if cnt != 1 or arr[-1] != 1:
        arr.insert(0, 1)
    else:
        arr.insert(0, 2)
    arr.pop()
    arr = sorted(arr)

    print(*arr)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_ints_in_list()
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
