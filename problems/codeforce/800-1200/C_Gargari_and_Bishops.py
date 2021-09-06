# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import random
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout

# -------------- INPUT FUNCTIONS ------------------

# sys.setrecursionlimit(2000)


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


def mark(grid, n, i, j):
    if i >= 0 and i < n and j >= 0 and j < n:
        if grid[i][j] == -1:
            return
        grid[i][j] = -1
        mark(grid, n, i-1, j-1)
        mark(grid, n, i-1, j+1)
        mark(grid, n, i+1, j-1)
        mark(grid, n, i+1, j+1)


def Solution(grid, n):
    # Write Your Code Here
    prefix = []
    for i in range(n):
        prefix.append([])
        for j in range(n):
            tl, tr = 0, 0
            if i > 0:
                if j > 0:
                    tl = prefix[i-1][j-1][0]+prefix[i-1][j-1][1]
                if j < n-1:
                    # print(prefix)
                    tr = prefix[i-1][j+1][2]+prefix[i-1][j+1][1]
            prefix[-1].append([tl, grid[i][j], tr])
    suffix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            bl, br = 0, 0
            if i < n-1:
                if j > 0:
                    bl = suffix[i+1][j-1][0]+suffix[i+1][j-1][1]
                if j < n-1:
                    br = suffix[i+1][j+1][2]+suffix[i+1][j+1][1]
            suffix[i][j] = [bl, grid[i][j], br]
    f = 0
    fidx = [1, 1]
    s = 0
    sidx = [1, 2]
    for i in range(n):
        for j in range(n):
            # if grid[i][j] == -1:
            #     continue
            p = sum(prefix[i][j])
            sf = sum(suffix[i][j])-suffix[i][j][1]
            if p+sf >= f:
                fidx = [i+1, j+1]
                # mark(grid, n, i, j)
                f = p+sf
                # print(p, s, "fdkf", i, j)
            # elif p+sf > s:
            #     sidx = [i+1, j+1]
            #     mark(grid, n, i, j)
            #     s = p+sf
                # print(f, s, "kjsfd", i, j)
    mark(grid, n, fidx[0]-1, fidx[1]-1)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == -1:
                continue
            p = sum(prefix[i][j])
            sf = sum(suffix[i][j])-suffix[i][j][1]
            if p+sf > s:
                sidx = [i+1, j+1]
            #     mark(grid, n, i, j)
                s = p+sf
                # print(f, s, "kjsfd", i, j)
    print(f+s)
    print(*[fidx[0], fidx[1], sidx[0], sidx[1]])


def main():
    # Take input Here and Call solution function
    n = get_int()
    grid = get_list_of_list(n)
    Solution(grid, n)


# calling main Function
if __name__ == '__main__':
    main()
