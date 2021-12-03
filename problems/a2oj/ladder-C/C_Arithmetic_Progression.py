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
    if n == 1:
        print(-1)
        return
    if n == 2:
        diff = abs(arr[1]-arr[0])
        if arr[1] != arr[0] and sum(arr) % 2 == 0:
            print(3)
            print(min(arr)-diff, sum(arr)//2, max(arr)+diff)
            return
    arr = sorted(arr)
    diffs = sorted([arr[i]-arr[i-1] for i in range(1, n)])
    if len(set(diffs)) == 1:
        if diffs[0] != 0:
            print(2)
            print(arr[0]-diffs[0], arr[-1]+diffs[0])
        else:
            print(1)
            print(arr[0])
        return
    if len(set(diffs)) > 2 or diffs[-1] != 2*diffs[-2]:
        print(0)
    else:
        for i in range(1, n):
            if arr[i]-arr[i-1] != diffs[0]:
                print(1)
                print(arr[i-1]+diffs[0])


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_ints_in_list()
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
