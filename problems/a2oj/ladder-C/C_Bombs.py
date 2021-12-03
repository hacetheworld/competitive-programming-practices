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
    res = []
    arr = sorted(arr, key=lambda x: x[2])
    # print(arr)
    for i in range(n):
        x, y = arr[i][0], arr[i][1]
        if x != 0:
            res.append([1, abs(x), "R" if x > 0 else "L"])
        if y != 0:
            res.append([1, abs(y), "U" if y > 0 else "D"])
        res.append([2])
        if x != 0:
            res.append([1, abs(x), "L" if x > 0 else "R"])
        if y != 0:
            res.append([1, abs(y), "D" if y > 0 else "U"])
        res.append([3])
    print(len(res))
    for itm in res:
        for c in itm:
            print(c, end=" ")
        print()


def main():
    # Take input Here and Call solution function
    n = get_int()
    axis = []
    for _ in range(n):
        x, y = get_ints_in_variables()
        sm = abs(x)+abs(y)
        axis.append([x, y, sm])

    Solution(axis, n)


# calling main Function
if __name__ == '__main__':
    main()
