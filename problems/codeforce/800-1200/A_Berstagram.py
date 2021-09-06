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


def Solution(arr, n, m):
    # Write Your Code Here
    hm = {}
    for i in range(1, n+1):
        hm[i] = [i, i, i]
    res = [i for i in range(n+1)]
    for j in range(m):
        post = arr[j]
        if hm[post][0] > 1:
            prev = hm[post][0]
            hm[post][0] = prev-1
            hm[post][1] = min(hm[post][1], prev-1)
            hm[res[prev-1]][0] = prev
            hm[res[prev-1]][2] = max(hm[res[prev-1]][2], prev)
            tmp = res[prev]
            res[prev] = res[prev-1]
            res[prev-1] = tmp
    for i in range(1, n+1):
        print(hm[i][1], hm[i][2])


def main():
    # Take input Here and Call solution function
    n, m = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, m)


# calling main Function
if __name__ == '__main__':
    main()
