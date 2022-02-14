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


def Solution(arr, n, s):
    # Write Your Code Here
    l = -1
    r = -1
    ans = 0
    j = 0
    for i in range(n):
        s += arr[i]
        while j < n and s < 0:
            s -= arr[j]
            j += 1
        if ans < (i-j+1):
            ans = i-j+1
            l = j+1
            r = i+1

    if ans == 0:
        print(-1)
    else:
        print(l, r)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, s = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, s)


# calling main Function
if __name__ == '__main__':
    main()
