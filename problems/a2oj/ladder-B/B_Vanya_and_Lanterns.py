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


def Solution(arr, n, l):
    # Write Your Code Here
    arr = sorted(arr)
    diff = -1
    for i in range(n-1):
        diff = max(diff, arr[i+1]-arr[i])
    ans = diff/2
    f = abs(arr[0]-0)
    l = abs(arr[-1]-l)
    if f > ans:
        ans += (f-ans)
    if l > ans:
        ans += (l-ans)
    print(ans)


def main():
    # Take input Here and Call solution function
    n, l = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, l)


# calling main Function
if __name__ == '__main__':
    main()
